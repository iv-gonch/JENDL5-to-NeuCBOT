import math
import os
import re
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SHOW_COMPOUND = True

el_z = {name: z for z, name in enumerate([
    'n', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al',
    'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca'], 1)}
z_el = {v: k for k, v in el_z.items()}


def compound_from_target(target):
    el, a = re.match(r'(\w+)-(\d+)', target).groups()
    return f'{z_el[el_z[el] + 2]}-{int(a) + 4}'


script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, 'reaction_masses.csv'), dtype={'Excitation energy': float})

reactions = df['Reaction'].unique()
n = len(reactions)

if SHOW_COMPOUND:
    x = [0, 1, 2, 3, 4]
    x_labels = ['', 'In', 'Compound', 'Out', '']
else:
    x = [0, 1, 2, 3]
    x_labels = ['', 'In', 'Out', '']


def draw_reaction(ax, m_in, m_comp, m_out, excitations):
    if SHOW_COMPOUND:
        ax.step(x, [0, m_in, 0, 0, 0], where='mid', color='black', linewidth=1)
        ax.step(x, [0, m_in + 10, 0, 0, 0], where='mid', color='black', linewidth=1, linestyle='--')
        ax.step(x, [0, 0, m_comp, 0, 0], where='mid', color='black', linewidth=1)
        ax.step(x, [0, 0, 0, m_out, 0], where='mid', color='black', linewidth=1)
        for e in excitations:
            if e == 0:
                continue
            ax.step(x, [0, 0, 0, m_out + e, 0], where='mid', color='black', linewidth=1)
        all_vals = [m_in, m_in + 10, m_comp, m_out] + [m_out + e for e in excitations if e > 0]
    else:
        ax.step(x, [0, m_in, 0, 0], where='mid', color='black', linewidth=1)
        ax.step(x, [0, m_in + 10, 0, 0], where='mid', color='black', linewidth=1, linestyle='--')
        ax.step(x, [0, 0, m_out, 0], where='mid', color='black', linewidth=1)
        for e in excitations:
            if e == 0:
                continue
            ax.step(x, [0, 0, m_out + e, 0], where='mid', color='black', linewidth=1)
        all_vals = [m_in, m_in + 10, m_out] + [m_out + e for e in excitations if e > 0]

    vmin = min(all_vals)
    vmax = max(all_vals)
    margin = max((vmax - vmin) * 0.15, 1.0)
    ax.set_ylim(vmin - margin, vmax + margin * 0.3)
    ax.set_xlim(0.9, len(x) - 1.9)
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x_labels, fontsize=9)
    ax.set_ylabel('E, MeV', fontsize=9)
    ax.grid(axis='y', alpha=0.3)


cols = 3
rows = math.ceil(n / cols)
fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
fig.subplots_adjust(hspace=0.4, wspace=0.3)
axes = axes.flatten() if n > 1 else [axes]

for idx, reaction in enumerate(reactions):
    ax = axes[idx]
    sub = df[df['Reaction'] == reaction]
    row = sub.iloc[0]
    draw_reaction(ax, float(row['In']), float(row['Compound']), float(row['Out']),
                  sorted(sub['Excitation energy'].unique()))
    parts = reaction.split(' → ')
    target = parts[0].split(' + ')[1].strip()
    compound = compound_from_target(target)
    ax.set_title(f'{parts[0]} → {compound} → {parts[1]}', fontsize=10)

for j in range(idx + 1, len(axes)):
    fig.delaxes(axes[j])

# fig.text(0.5, 0.01, 'Время', ha='center', fontsize=11)
plt.savefig(os.path.join(script_dir, 'level_schemes.png'), dpi=150, bbox_inches='tight')

indiv_dir = os.path.join(script_dir, 'level_schemes_indiv')
os.makedirs(indiv_dir, exist_ok=True)

for idx, reaction in enumerate(reactions):
    sub = df[df['Reaction'] == reaction]
    row = sub.iloc[0]
    fig_i, ax_i = plt.subplots(figsize=(4, 5))
    draw_reaction(ax_i, float(row['In']), float(row['Compound']), float(row['Out']),
                  sorted(sub['Excitation energy'].unique()))
    parts = reaction.split(' → ')
    target = parts[0].split(' + ')[1].strip()
    compound = compound_from_target(target)
    ax_i.set_title(f'{parts[0]} → {compound} → {parts[1]}', fontsize=10)
    # ax_i.set_xlabel('Время', fontsize=11)

    fname = reaction.replace(' ', '_').replace('→', '->').replace('+', 'plus')
    fig_i.savefig(os.path.join(indiv_dir, f'{fname}.png'), dpi=150, bbox_inches='tight')
    plt.close(fig_i)

print('Done. Saved combined plot and', len(reactions), 'individual plots.')
