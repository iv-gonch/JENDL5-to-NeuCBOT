import urllib.request
import urllib.error
import re
import csv
import time

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'

ISOTOPES = [
    (0, 1, 'n'), (1, 1, 'H'), (2, 4, 'He'),
    (3, 6, 'Li'), (3, 7, 'Li'), (4, 9, 'Be'),
    (5, 10, 'B'), (5, 11, 'B'), (6, 12, 'C'), (6, 13, 'C'),
    (7, 14, 'N'), (7, 15, 'N'), (8, 16, 'O'), (8, 17, 'O'), (8, 18, 'O'),
    (9, 17, 'F'), (9, 18, 'F'), (9, 19, 'F'),
    (10, 20, 'Ne'), (10, 21, 'Ne'), (10, 22, 'Ne'),
    (11, 22, 'Na'), (11, 23, 'Na'),
    (13, 26, 'Al'), (13, 27, 'Al'),
    (14, 28, 'Si'), (14, 29, 'Si'), (14, 30, 'Si'),
    (15, 30, 'P'), (15, 31, 'P'),
    (16, 31, 'S'), (16, 32, 'S'),
    # extra from chemistry.py
    (5, 7, 'B'), (5, 8, 'B'), (5, 9, 'B'),
    (6, 10, 'C'), (7, 11, 'N'), (7, 12, 'N'), (7, 13, 'N'),
    (8, 13, 'O'), (8, 14, 'O'), (8, 15, 'O'),
    (9, 15, 'F'), (9, 16, 'F'),
    (10, 17, 'Ne'), (10, 18, 'Ne'), (10, 19, 'Ne'),
    (11, 20, 'Na'),
    (13, 24, 'Al'),
    (14, 31, 'Si'),
    (16, 33, 'S'), (16, 34, 'S'),
]

def get_element_symbol(z):
    symbols = {0: 'n', 1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C',
               7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al',
               14: 'Si', 15: 'P', 16: 'S'}
    return symbols.get(z, '')

def fetch_nudat3(nucleus_str):
    url = f"https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus={nucleus_str}&unc=NDS"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as f:
        return f.read().decode('utf-8')

def extract_text(td_html):
    text = re.sub(r'<[^>]+>', ' ', td_html)
    text = text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&times;', 'x').replace('&asymp;', '~')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_halflife(t12_text):
    result = {'halflife': '', 'halflifeUnit': '', 'halflifeUncertainty': '',
              'decayMode': '', 'branchingRatio': '', 'branchingRatioUncertainty': ''}

    if not t12_text:
        return result

    if 'STABLE' in t12_text:
        result['halflife'] = 'STABLE'
        return result

    parts = t12_text.split('%')
    t12_part = parts[0].strip()

    m = re.match(r'([\d.]+(?:x10[-\d]*)?)\s*(\w+)\s*(\d+)', t12_part)
    if m:
        result['halflife'] = m.group(1)
        result['halflifeUnit'] = m.group(2)
        result['halflifeUncertainty'] = m.group(3)
    else:
        m2 = re.match(r'([\d.]+(?:x10[-\d]*)?)\s*(\w+)', t12_part)
        if m2:
            result['halflife'] = m2.group(1)
            result['halflifeUnit'] = m2.group(2)

    decay_modes = []
    for p in parts[1:]:
        p = p.strip()
        dm = re.match(r'\s*(\w+)\s*=\s*([\d.]+(?:x10[-\d]*)?)', p)
        if dm:
            decay_modes.append(f"%{dm.group(1)}={dm.group(2)}")
    result['decayMode'] = '; '.join(decay_modes)
    return result

def parse_page(html):
    result = {'qvals': {}, 'levels': []}

    # Q-values from header
    for name, pattern in [
        ('Q(beta-)', r'Q\(β-\)=\s*([-\d.]+)\s*keV\s*(\d*)'),
        ('Q(beta+)', r'Q\(β\+\)=\s*([-\d.]+)\s*keV\s*(\d*)'),
        ('Q(EC)', r'Q\(EC\)=\s*([-\d.]+)\s*keV\s*(\d*)'),
        ('S(n)', r'S\(n\)=\s*([-\d.]+)\s*keV\s*(\d*)'),
        ('S(p)', r'S\(p\)=\s*([-\d.]+)\s*keV\s*(\d*)'),
        ('Q(alpha)', r'Q\(α\)=\s*([-\d.]+)\s*keV\s*(\d*)'),
    ]:
        m = re.search(pattern, html)
        if m:
            result['qvals'][name] = (float(m.group(1)), float(m.group(2)) if m.group(2) else 0.0)

    # Main table: find <table id="mainTable">
    ts = html.find('<table id="mainTable"')
    if ts < 0:
        return result

    # find matching </table>
    te = ts
    depth = 0
    while te < len(html):
        op = html.find('<table', te + 1)
        cp = html.find('</table>', te + 1)
        if op >= 0 and op < cp:
            depth += 1
            te = op + 7
        elif cp >= 0:
            if depth <= 0:
                te = cp + 8
                break
            depth -= 1
            te = cp + 8
        else:
            break

    table_html = html[ts:te]

    # Iterate over all rows in the table
    pos = 0
    while True:
        tr_start = table_html.find('<tr', pos)
        if tr_start < 0:
            break
        tr_end = table_html.find('</tr>', tr_start)
        if tr_end < 0:
            break
        row_html = table_html[tr_start:tr_end + 5]
        pos = tr_end + 5

        # Only process rows with level data (containing cell elvl)
        if 'cell elvl' not in row_html:
            continue

        # Split the row into groups of <td> cells
        # Each level has ~9 cells: elvl, xref, jpi, t12, gamm, ints, mult, fin, fin
        td_positions = []
        tpos = 0
        while True:
            td_start = row_html.find('<td', tpos)
            if td_start < 0:
                break
            td_end = row_html.find('</td>', td_start)
            if td_end < 0:
                break
            td_positions.append((td_start, td_end + 5))
            tpos = td_end + 5

        # Process the SINGLE row containing all levels as cell groups
        i = 0
        while i + 8 < len(td_positions):
            elvl_td = row_html[td_positions[i][0]:td_positions[i][1]]
            jpi_td = row_html[td_positions[i+2][0]:td_positions[i+2][1]]
            t12_td = row_html[td_positions[i+3][0]:td_positions[i+3][1]]

            if 'cell elvl' not in elvl_td:
                break

            energy_text = extract_text(elvl_td)
            energy_str = energy_text.split()[0] if energy_text else '0'
            try:
                energy_kev = float(energy_str.replace('x', 'e').replace('−', '-'))
            except ValueError:
                break

            jpi_text = extract_text(jpi_td)
            t12_text = extract_text(t12_td)
            hlf = parse_halflife(t12_text)

            result['levels'].append({
                'energy_kev': energy_kev,
                'jpi': jpi_text,
                'halflife': hlf['halflife'],
                'halflifeUnit': hlf['halflifeUnit'],
                'halflifeUncertainty': hlf['halflifeUncertainty'],
                'decayMode': hlf['decayMode'],
            })
            i += 9

    return result


def main():
    results = []
    processed = set()

    for z, a, symbol in ISOTOPES:
        key = (z, a)
        if key in processed:
            continue
        processed.add(key)

        nucleus_str = f"{a}{get_element_symbol(z)}"
        total_unique = len(set((zz, aa) for zz, aa, _ in ISOTOPES))
        print(f"  [{len(processed)}/{total_unique}] Fetching {nucleus_str}...", end='', flush=True)

        try:
            html = fetch_nudat3(nucleus_str)
            parsed = parse_page(html)
            qvals = parsed['qvals']
            levels = parsed['levels']

            sn = qvals.get('S(n)', (None, None))
            sp = qvals.get('S(p)', (None, None))
            qa = qvals.get('Q(alpha)', (None, None))

            gs = levels[0] if levels else {}

            first_exc = None
            for lev in levels:
                if lev['energy_kev'] > 0.001:
                    first_exc = lev
                    break

            # ground state row
            results.append({
                'z': z, 'n': a - z, 'name': symbol, 'levelEnergy(MeV)': 0.0,
                'halflife': gs.get('halflife', ''),
                'halflifeUnit': gs.get('halflifeUnit', ''),
                'halflifeUncertainty': gs.get('halflifeUncertainty', ''),
                'spinAndParity': gs.get('jpi', ''),
                'decayMode': gs.get('decayMode', ''),
                'branchingRatio': '', 'branchingRatioUncertainty': '',
                'massExcess(keV)': '', 'massExcessUncertainty': '',
                'neutronSeparationEnergy': sn[0] if sn[0] is not None else '',
                'neutronSeparationEnergyUncertainty': sn[1] if sn[0] is not None else '',
                'protonSeparationEnergy': sp[0] if sp[0] is not None else '',
                'protonSeparationEnergyUncertainty': sp[1] if sp[0] is not None else '',
                'alpha': qa[0] if qa[0] is not None else '',
                'alphaUncertainty': qa[1] if qa[0] is not None else '',
                'bindingEnergy': '', 'bindingEnergyUncertainty': '',
                'firstExcitedStateEnergy': first_exc['energy_kev'] / 1000.0 if first_exc else '',
                'firstExcitedStateEnergyUncertainty': '',
            })

            # excited states
            for lev in levels[1:]:
                results.append({
                    'z': z, 'n': a - z, 'name': symbol,
                    'levelEnergy(MeV)': lev['energy_kev'] / 1000.0,
                    'halflife': lev.get('halflife', ''),
                    'halflifeUnit': lev.get('halflifeUnit', ''),
                    'halflifeUncertainty': lev.get('halflifeUncertainty', ''),
                    'spinAndParity': lev.get('jpi', ''),
                    'decayMode': lev.get('decayMode', ''),
                    'branchingRatio': '', 'branchingRatioUncertainty': '',
                    'massExcess(keV)': '', 'massExcessUncertainty': '',
                    'neutronSeparationEnergy': '', 'neutronSeparationEnergyUncertainty': '',
                    'protonSeparationEnergy': '', 'protonSeparationEnergyUncertainty': '',
                    'alpha': '', 'alphaUncertainty': '',
                    'bindingEnergy': '', 'bindingEnergyUncertainty': '',
                    'firstExcitedStateEnergy': '', 'firstExcitedStateEnergyUncertainty': '',
                })

            print(f" {len(levels)} levels", flush=True)

        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f" NOT FOUND", flush=True)
            elif e.code == 429:
                print(f" RATE LIMITED", flush=True)
                time.sleep(10)
            else:
                print(f" HTTP {e.code}", flush=True)
        except Exception as e:
            print(f" ERROR: {e}", flush=True)

        time.sleep(1.5)

    fieldnames = [
        'z', 'n', 'name', 'levelEnergy(MeV)',
        'halflife', 'halflifeUnit', 'halflifeUncertainty',
        'spinAndParity', 'decayMode', 'branchingRatio', 'branchingRatioUncertainty',
        'massExcess(keV)', 'massExcessUncertainty',
        'neutronSeparationEnergy', 'neutronSeparationEnergyUncertainty',
        'protonSeparationEnergy', 'protonSeparationEnergyUncertainty',
        'alpha', 'alphaUncertainty',
        'bindingEnergy', 'bindingEnergyUncertainty',
        'firstExcitedStateEnergy', 'firstExcitedStateEnergyUncertainty',
    ]

    with open('nudat3_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(results)

    print(f"\nDone! {len(results)} entries written to nudat3_data.csv")

if __name__ == '__main__':
    main()
