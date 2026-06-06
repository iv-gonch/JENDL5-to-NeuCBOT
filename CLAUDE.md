# JENDL5-to-NeuCBOT — Technical Reference for AI Agents

## Project Purpose

Converts JENDL-5 Alpha-particle sublibrary (ENDF-6 format) into NeuCBOT-compatible neutron spectral data for (α,n) reactions. Given an incident alpha energy and target isotope, the pipeline produces the double-differential neutron yield d²σ/(dE_n dΩ) integrated over all angles, on a uniform energy grid.

---

## File Map

| File | Role |
|------|------|
| `main.py` | Entry point; argument parsing; defines `MT_list`; dispatches per-MT pipeline |
| `converter.py` | Parses ENDF-6 FORTRAN text → pipe-delimited files; separates by MF/MT |
| `processor.py` | Legendre expansion → angular distribution → 2-body kinematics → E_n spectrum |
| `adjuster.py` | Interpolates variable-grid data to uniform (E_α, E_n) grid; writes NeuCBOT output |
| `make_MT4_dir.py` | Sums MT≥50 partial spectra and XS → MT=4 total reaction |
| `chemistry.py` | Atomic mass lookup; `getMass()`, `getMassExited()`, `getZ()`, `getElement()` |
| `constants.py` | ENDF-6 column layout (`ENDF` class); physical constants (`physics` class) |

---

## Mass Unit System — Critical

`chemistry.masses` stores values in **neutron mass units**: `value = M_atomic_amu / m_n_amu`

- `m_n_amu = 1.00866491595` a.m.u. (AME2020)
- `getMass(ZA)` returns in **eV**: `masses[key] × 939_565_421`
- **All masses are atomic** (include electron masses). Using nuclear masses instead of atomic
  causes Q-value errors of Z_product × 0.511 MeV.
- Excited states: `masses['Z-El-A*N'] = ground_value + E_excit_eV / 939_565_421`
  where `E_excit_eV` is the excitation energy in eV.

### MT → excited state mapping in `chemistry.py`

```
MT=50  → key '...*0'  (ground state, same as base key)
MT=51  → key '...*1'  (1st excited state)
MT=52  → key '...*2'
...
```

`getMassExited(ZA, MT)` uses `MT - 50` as the excited-state index.

### How to add a new nucleus to chemistry.py

1. Add ground-state atomic mass to `masses_from_AME2020` in a.m.u.
2. Compute the `masses` entry: `M_amu / 1.00866491595`. Must be **atomic** mass.
3. Add excited states as `'Z-El-A*N': ground + E_keV * 1000 / 939_565_421`
4. Check: `getMass(ZA) / 939_565_421 * 931.494` should equal your AME2020 a.m.u. value.

---

## Pipeline Stages and Directories

```
jendl5-a/a_ZZZ-El-AAA.dat        ← raw ENDF-6 input (JENDL-5 Alpha sublibrary)
    │
    ▼  converter.convertENDF(fname)
stage_1_data/converted/El_A       ← pipe-delimited ENDF, one file per isotope

    │
    ▼  converter.separateData(fname, MT)
stage_1_data/reshaped/El_A/
    ├── MF3_MT<MT>                 ← cross-section: E_α [eV]  σ [barn]
    └── MF6_MT<MT>/NK1_NE<i>      ← Legendre coefficients for i-th incident energy

    │
    ▼  processor.getEnergyAngleDistribtion(fname, MT, points, normcheck)
stage_1_data/angle_distribution/El_A/MF6_MT<MT>/NK1_NE<i>
    │                              ← cos θ  p(cos θ)  (101 points)
    │
    └─ processor.angle2spectrum(...)
stage_1_data/En_distribution/El_A/MF6_MT<MT>/NK1_NE<i>
                                   ← E_n [eV]  p(E_n) [1/eV]  (101 points)

    │
    ▼  adjuster.neucbotIn(fname, MT, points, dE_a, dE_n)
stage_2_data/<El>/<El_A>/JendlOut/MT<MT>/
    ├── cross-section              ← E_α [MeV]  σ [mb]; 0–15 MeV, step dE_a
    └── outputE<X.XXXX>           ← E_n [MeV]  p(E_n)·σ [1/MeV]; step dE_n

(also copied to ../neucbot/Data/Isotopes/<El>/<ElA>/JendlOut/ if that path exists)
```

---

## Supported Isotopes (MT_list in main.py)

| Isotope | Reaction | MT channels | Residual nucleus |
|---------|----------|-------------|------------------|
| Li_6 | ⁶Li(α,n)⁹B | 50–53 | B-9 |
| Li_7 | ⁷Li(α,n)¹⁰B | 50–54 | B-10 |
| Be_9 | ⁹Be(α,n)¹²C | 50–52 | C-12 |
| B_10 | ¹⁰B(α,n)¹³N | 50–54 | N-13 |
| B_11 | ¹¹B(α,n)¹⁴N | 50–54 | N-14 |
| C_12 | ¹²C(α,n)¹⁵O | 50 only | O-15 |
| C_13 | ¹³C(α,n)¹⁶O | 50–54 | O-16 |
| N_14 | ¹⁴N(α,n)¹⁷F | 50–54 | F-17 |
| N_15 | ¹⁵N(α,n)¹⁸F | 50–54 | F-18 |
| O_17 | ¹⁷O(α,n)²⁰Ne | 50–53 | Ne-20 |
| O_18 | ¹⁸O(α,n)²¹Ne | 50–54 | Ne-21 |
| F_19 | ¹⁹F(α,n)²²Na | 50–77 | Na-22 |
| Na_23 | ²³Na(α,n)²⁶Al | 50–78 | Al-26 |

---

## Key Function Signatures

### chemistry.py

```python
getMass(ZA: int) -> float
# ZA = Z*1000 + A. Returns atomic mass in eV (= masses[key] * 939_565_421).
# Raises KeyError if isotope not in masses dict.

getMassExited(ZA: int, MT: int) -> float
# Returns mass of residual nucleus in excited state MT (uses MT-50 as level index).
# Returns same as getMass for MT=50 (ground state).

getZ(ele: str) -> int
# Element symbol (case-insensitive) → atomic number Z.

getElement(z: int) -> str
# Atomic number → element symbol, or "None" if not found.
```

### converter.py

```python
convertENDF(fname: str)
# fname: isotope name, e.g. "C_13". Reads jendl5-a/a_ZZZ-El-AAA.dat.
# Writes stage_1_data/converted/fname.

separateData(fname: str, MT: int)
# Extracts MF=3 (XS) and MF=6 (Legendre) data for reaction MT.
# Writes stage_1_data/reshaped/fname/MF3_MT{MT} and MF6_MT{MT}/NK1_NE*.
```

### processor.py

```python
getLegendre(points: int, lmax: int) -> np.ndarray  # shape [points, lmax]
# Legendre polynomials P_l(x) for x in linspace(-1, 1, points).

legendre2angle(Coeff: list, points: int, NE: int) -> np.ndarray  # shape [NE, points]
# p(cos θ) = Σ_l (2l+1)/2 * C_l * P_l(cos θ)

angle2spectrum(fname, MT, points, NK, NE, E_in, dist_angle, isData)
# Core kinematics. Writes angle_distribution and En_distribution files.
# Q-value: Q = (M_target + M_alpha - M_residual - M_neutron) in eV

getEnergyAngleDistribtion(fname: str, MT: int, points: int, normcheck: bool)
# Orchestrates: reads Legendre → legendre2angle → angle2spectrum.
```

### adjuster.py

```python
RebinXS(fname: str, MT: int, dE_a: float) -> np.ndarray
# Reads MF3_MT cross-section, rebins to uniform dE_a grid, converts barn→mb.
# Returns XS array in mb.

interpolation(E_aBase, E_nBase, distBase, points, dE_a, dE_n)
# 2D interpolation: variable JENDL grid → uniform (E_α, E_n) grid.
# Returns E_aRebin, E_nRebin, distRebin.

neucbotIn(fname: str, MT: int, points: int, dE_a: float, dE_n: float)
# Full stage-2 pipeline: reads En_distribution, interpolates, multiplies by XS,
# writes stage_2_data and (if path exists) ../neucbot/Data/Isotopes/.
```

### make_MT4_dir.py

```python
summ_dataXS(fname: str)      # Accumulates XS: MT4 = MT50 + MT51 + ...
summ_dataOutputE(fname: str)  # Accumulates spectra: same sum over MT
main()                         # Hardcoded for C_13 only — generalize before reuse
```

---

## Kinematic Formula (processor.py:125–146)

Non-relativistic two-body kinematics in the lab frame (α + A → B + n):

```python
eqA = a + In + T_a[i]
eqB = cos_Theta[j] * np.sqrt(a * T_a[i] * n)
eqC = (Out**2. - (In + a - n)**2.) / 2. - T_a[i] * (In - n)
T_n[i, j] = ((eqB + np.sqrt(eqB**2. - eqA * eqC)) / eqA)**2.
```

Variables (all in eV, masses in eV via getMass):
- `a` = M_He4 (alpha), `n` = M_neutron, `In` = M_target, `Out` = M_residual
- `T_a[i]` = incident alpha kinetic energy; `T_n[i,j]` = outgoing neutron energy
- `Out` uses `getMassExited` for MT≠50, incorporating excitation energy

Threshold (for Q < 0):
```python
E_treshold_lab = -Q * (1. + a/In - Q/(2.*In))
```

---

## How to Run

```bash
# Single isotope (processes all MT channels for that nucleus)
python3 main.py -nucleus C_13

# With custom grid resolution
python3 main.py -nucleus O_17 -points 201 -dE_a 5000 -dE_n 50000

# All isotopes sequentially (outdated script, uses old -MT syntax)
bash script.sh

# Create total MT=4 directory (hardcoded for C_13)
python3 make_MT4_dir.py

# Clean NeuCBOT side
bash NeuCBOT_clear_JENDL.sh
```

Arguments (single-dash syntax):
- `-nucleus NAME` — required; isotope key from MT_list (e.g. `C_13`, `O_17`)
- `-points N` — angular grid points (default 101); must be odd for symmetry
- `-dE_a E` — alpha energy bin in eV (default 1e4 = 10 keV)
- `-dE_n E` — neutron energy bin in eV (default 1e5 = 100 keV)

---

## ENDF-6 Format Notes

JENDL-5 files in `jendl5-a/a_ZZZ-El-AAA.dat` use fixed-width FORTRAN format:
- Columns 1–66: six 11-char numerical fields (C1…C6)
- Columns 67–70: MAT (material number)
- Columns 71–72: MF (file type: 3=XS, 6=energy-angle)
- Columns 73–75: MT (reaction type)
- Columns 76–80: NS (line number)

`convertENDF()` adds `|` delimiters and fixes Fortran exponential notation (`+0.0+0` → `+0.0e+0`).

`separateData()` validates: LAW=2 (Legendre), LCT=2 (lab frame), NK=1 (one outgoing particle). Warns on LANG≠0.

---

## Output Format (stage_2_data)

**`cross-section` file:**
```
# E_a, MeV    XS, mb
0.0           0.0
0.01          0.0
...
15.0          <value>
```
Step = dE_a (default 0.01 MeV). Values below threshold are zero.

**`outputE<X.XXXX>` file** (one per incident alpha energy):
```
# Incident particle energy (MeV) =
# 5.00
#
# En.lab,MeV distribution
   0.100000  <value>
   0.200000  <value>
...
```
Units: E_n in MeV, distribution in mb/MeV (= XS × p(E_n), so ∫distribution dE_n = σ(E_α) in mb).
File contains `EMPTY` if E_α is outside JENDL data range or XS = 0.

---

## Known Fixed Bugs

**Commit bfb1ee5 (2026-06-05):** Eight product nuclei in `chemistry.masses` were stored as
**nuclear masses** (missing Z_product × m_e ≈ Z × 0.511 MeV) instead of atomic masses.

Affected nuclei: O-15, F-17, F-18, Ne-20, Ne-21, Na-22, Al-26, S-31  
Affected reactions: ¹²C, ¹⁴N, ¹⁵N, ¹⁷O, ¹⁸O, ¹⁹F, ²³Na, ²⁸Si  
Error magnitude: +4.1 to +8.2 MeV on Q-value → wrong threshold energies and wrong minimum E_n  
Fix: replaced 8 ground-state values and all corresponding excited states with correct atomic masses from AME2020.

Also fixed: `masses_from_AME2020['11-Na-20']` was erroneously set to Ne-20's mass (19.992440 a.m.u.);
corrected to 20.0073544 a.m.u. The `masses['11-Na-20']` entry was already correct.

---

## Adding a New Isotope

1. Place ENDF-6 file in `jendl5-a/` following naming convention `a_ZZZ-El-AAA.dat`.
2. In `chemistry.py`:
   - Add to `masses_from_AME2020`: `'Z-El-A': <AME2020 value in a.m.u.>`
   - Add to `masses` (ground state): `'Z-El-A': <AME2020_amu / 1.00866491595>`
   - Add excited states: `'Z-El-A*N': <ground> + <E_keV * 1000 / 939_565_421>`
   - Must use **atomic** mass (not nuclear).
3. Add the residual nucleus (Z+2, A+3) to `chemistry.masses` similarly.
4. Add entry to `MT_list` in `main.py`: `"El_A": [50, 51, ...]`
5. Run `python3 main.py -nucleus El_A` and verify Q-values match AME2020.
