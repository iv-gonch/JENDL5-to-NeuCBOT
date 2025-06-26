# JENDL5 to NeuCBOT                     
Author: Ivan Goncharenko

email: iv.gonch.0907@gmail.com

Date: 12 Mar 2025

github: https://github.com/iv-gonch/JENDL5-to-NeuCBOT

# JENDL5-to-NeuCBOT (Japanese Evaluated Nuclear Data Library 5 to Neutron Calculator Based On TALYS)     

## TABLE OF CONTENTS

1. [About JENDL5-to-NeuCBOT](#about)
  - i. [General](#general)
  - ii [Dependencies](#dependencies)
  - iii [Directory Structure](#directory-structure)
  - iv [Calculationa](#calculations)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Output](#Output)
5. [Citations](#citations)

---
---
## 1. <a id="about">About JENDL5-to-NeuCBOT</a>
### i. <a id="general">General</a>

JENDL5-to-NeuCBOT is a tool for evaluating differential neutron spectra $\ \sigma(E_\alpha)\cdot \text{d}E_\alpha\ $ and double differential neutron spectra $\ \sigma(E_\alpha, E_n)\cdot \text{d}E_\alpha \text{d}E_n\ $ from [JENDL5](https://wwwndc.jaea.go.jp/jendl/j5/j5.html) for adding them into [NeuCBOT](https://github.com/shawest/neucbot), which is a tool for calculating ($\alpha$,n) yields and neutron spectra for arbitrary materials under alpha exposure for arbitrary lists of alpha energies or in the presence of alpha-emitting contaminants.

### ii. <a id="dependencies">Dependencies</a>
This software was written in Python 3.12.6. 
To the extent that some scripts included in this package rely on bash, was written for bash 5.2.15.

This code itself doesn't do anything particularly fancy, and so it will likely work on systems running different versions of Python and bash.

Before running the code you may need to download numpy and scipy libraries by running in your terminal these lines:
```bash
pip3 install numpy
pip3 install scipy
```

If you don't have pip3, just look online for how to install it for your Operating System (OS).

### iii. <a id="directory-structure">Directory Structure</a>

JENDL files for reactions with incoming alpha particle are stored in the ./jendl5-a directory separately for each isotope. 
These files use the ENDF-6 file structure, so should be read in agreement with [ENDF-6 Formats Manual](https://www-nds.iaea.org/public/endf/endf-manual.pdf).
Files contain cross sections (MF = 3), and energy-angle distributions of emitted particles (MF = 6) for ($\alpha$,n) (MT = 4) and ($\alpha$,n') reactions (MT = 50 - 91). 
JENDL dataset provides information on the partial reactions, where 
* MT50 stands for ($\alpha$,$\text{n}_0$) of reaction with the 
residual nucleus in ground state
* MT51 stands for ($\alpha$,$\text{n}_1$) of reaction with the 
residual nucleus in the $1^{\text{st}}$ exited state

&emsp;&emsp;&emsp; $\cdot \cdot \cdot$
* MT[50+X] stands for ($\alpha$,$\text{n}_X$) of reaction with 
the residual nucleus in the $\text{X}^{\text{st}}$ exited state
* MT4 stands for ($\alpha$,n) reaction in general and exactly 
equal to a summ of all partial reactions 

Each /MT␣/ directory contains differential by alpha energy cross section file called /cross-section, which is used for neutron yeild calculations. 
This files were structured in the TALYS format so the neucbot programm could make all the calculations with minimal changes.

Also each /MT␣/ directory contains double differential by alpha and by neutron energies cross section files called /outputE␣, for each alpha energy. 
It is used for calculating neutron spectrum.

While running the code new directories will be created.
Since the ENDF-6 format is adapted to the FORTRAN programming language, ./stage_1_data/converted/ directory is created for the convenience of reading files using Python.
Than ./stage_1_data/reshaped/ directory is created as reference files that don't have the inconvenient ENDF-6 format.

JENDL files store energy-angle distributions of emitted particles using Legendre polynomials. 
./stage_1_data/angle_distribution/ directory contains angle distributions as a function of dependence on the cosine of the emitted particle. 
Than, via kinematics neutrin energy distributions are obtained and stored in ./stage_1_data/En_distribution/ directory.

Result is stored in ./stage_2_data/ directory in the NeuCBOT-applicable shape.
Also all the data will be automatically stored in the neucbot directory if ./JENDL5-to-NeuCBOT directory is plased next to the ./neucbot directory.

For questions or comments, feel free to send me an email.

### iii. <a id="calculations">Calculations</a>

Compaund nucleus theory approach,

2 -> 1 -> 2 body kinematics, (see./alpha_n_stuff/Вывод кинематики.pdf)

classic approach (?)

Interpolation problems

---
---

## 2. <a id="setup">Setup</a>

The code for NeuCBOT is stored in 
<https://github.com/shawest/neucbot>.

The code for JENDL5-to-NeuCBOT is stored in 
<https://github.com/iv-gonch/JENDL5-to-NeuCBOT>.

To access the code, you can either download it directly by clicking the "Clone or download" button and choosing "Download ZIP", or checking out the repository with the command

```bash
git clone https://github.com/iv-gonch/JENDL5-to-NeuCBOT
```

This will create a directory called JENDL5-to-NeuCBOT in your current directory.
For full-fledged use of the code, clone it next to the ./neucbot directory.

Before start use script "clear_JENDL.sh" by running
```bash
bash clear_JENDL.sh
```

It will remove all the JENDL data from the ./neucbot directory and clear ./stage_1_data/ and ./stage_2_data/ directories. 

---
---

## 3. <a id="usage">Usage</a>

JENDL5-to-NeuCBOT can be run from the command line of any unix-based operating system with the command

```bash
bash script.sh
```

where the list of options is a series of parameters given. 
Each option starts with a double hyphen and is followed by any arugments needed by that option.

A list of arguments is given below, follwed by parameters
required by that option (written in square brackets) and
a description of what that option does in parentheses.

* --points \[integer\] (the number of points in the primary distribution energy-angle distribution functions)
* --dE_a \[integer\] (the size of the output alpha particle energy bin, eV)
* --dE_n \[integer\] (the size of the output neutron energy bin, eV)
* --nucleus \[Element_A\] (name of the target nucleus of the calculated ($\alpha$,$\text{n}$) reaction)

In order to run JENDL-to-NeuCBOT, the user must enter target nucleus of the ($\alpha$,$\text{n}$) reaction (--nucleus Na_23).

All other options are optional. 

* If the --points option is not specified, a default value 101 will be assumed.
* If the --dE_a option is not specified, a default bin size 10 keV will be assumed.
* If the --dE_a option is not specified, a default bin size 0,1 MeV will be assumed.

Example usage of JENDL5-to-NeuCBOT is given below

```bash
python3 ./main.py --nucleus C_13
```

It should be noted that the order of these options does not 
matter.

If any isotopes listed in the material composition description 
are not present in the ($\alpha$,n) reaction library, NeuCBOT 
will throw an error.

This section describes the anatomy of a material composition 
file. One such file must be given to NeuCBOT as an argument to
the -m option.

These text files consist of four columns. 

The first column is the chemical symbol of an element in 
the material. Capitalization does not matter.

The second column is the mass number of this isotope. If
0 is specified, it will be assumed that all naturally 
occurring isotopes of this element are present at their
natural abundances, as reported in [\[4\]](#4).

The third column is the percent mass of the specified
element or isotope.

The fourth column is the basename: empty or "t" for TALYS and
"j" for JENDL.

For example
> c 12 45
>
> c 13 55

would describe a material that is made of 45% <sup>12</sup>C
and 55% <sup>13</sup>C, by mass.

More realistically,

> c 0 59.984
>
> o 0 31.962
>
> h 0 8.054

is the composition of acrylic, assuming carbon, oxygen, and
hydrogen isotopes are all present according to their natural
abundances.

After reading a material composition file, NeuCBOT normalizes
the composition so that all isotopes add up to 100%. The
user may therefore specify mass fractions as percentages or
decimals, as they prefer.

All lines in this file that start with a \# are skipped
by NeuCBOT, allowing the user to leave comments in these 
files.

Decay chains are specified in text files with two columns.

The first column specifies the name of the isotope, which
is the chemical symbol followed by the mass number, and
the second column is the percent of decays of the chain
in which the specified isotope occurs, relative to the 
top of the chain.

It is important to note that the second column must be
given in <b>percent</b> probability of the isotope 
appearing.

As an example, the <sup>232</sup>Th decay chain is specified
as

> Th232 100
>
> Th228 100
>
> Ra224 100
>
> Rn220 100
>
> Po216 100
>
> Bi212 35.94
>
> Po212 64.06

Similar to the material composition description, lines that
start with a \# are skipped by NeuCBOT.

Alpha list files are structured very similiarly to isotope 
list files.

Each text file has two columns. The first column specifies
an alpha energy in MeV, and the second column specifies the 
<b>percent</b> porbability of an alpha of that energy being
produced.

For example, <sup>216</sup>Po alphas can be described with
a file that reads as

> 6.7783 99.9981
>
> 5.985 0.0019

Like in the two above cases, lines that start with a \# 
are skipped by NeuCBOT.

---
---
## 4. <a id="output">Output</a>
The output of NeuCBOT is hopefully mostly straightforward to 
understand. 

As NeuCBOT runs, it prints the alpha energy every 10 keV, so 
its progress can be tracked. It will also output any relevant 
warnings it may encounter while running. The most likely 
warnings will be missing isotopic data in the ($\alpha$,n) 
database. If the alpha energies simulated are all under 10 MeV 
and only naturally occuring isotopes are being simulated, the 
simplest solution is to run NeuCBOT with the -d option, an it 
will acquire ($\alpha$,n) data automatically. Otherwise, the 
user should install TALYS and run with the -t option.

The output provides the total neutron yield, calculated by 
integrating all of ($\alpha$,n) cross sections over the tracks 
of the alphas as they slow down. The units used here are the 
number of neutrons produced per decay of the entire decay 
chain or list of alpha energies being simulated. So if a chain 
has three alpha-emitting isotopes, NeuCBOT tells you the 
expected number of neutrons after all three isotopes have 
decayed with their given branching ratios.

NeuCBOT also gives a breakdown of the contribution of each 
isotope in the target material to the total neutron yield.

Due to effects of binning the neutron energy spectrum and 
inaccuracies of Riemann integration, it is possible that the 
integral of the neutron energy spectrum will be slightly 
different from the total neutron yield. These differences are 
typically under ~1%. We therefore include the integral of the 
neutron energy spectrum in the output.

Lastly, the neutron energy spectrum is printed. By default, 
the spectrum is binned into 100 keV bins and the spectrum is 
given in units of $\ \cfrac{\text{neutron}}{\text{decay} \cdot 100\ \text{keV}}\ $.

---
---
## 5. <a id="citations">Citations</a>
1. <a id="1">O. Iwamoto, et al. Japanese evaluated nuclear data library version 5: JENDL-5. http://www.talys.eu/</a>
2. <a id="2">J. Ziegler, et al. SRIM-2008. http://www.srim.org/</a>
3. <a id="3">J. K. Tuli, et al. Evaluated Nuclear Structure Data File (ENSDF), 1996.</a>
4. <a id="4">P. De Bievre and P.D.P. Taylor, Int. J. Mass Spectrom. Ion Phys. 123, 149 (1993).</a>