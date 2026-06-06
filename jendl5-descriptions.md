# Li-6  (Z=3, A=6)
**File:** `a_003-Li-006.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `3006` | Target nucleus: Li-6 |
| AWR | `5.96345` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `129` | Lines of descriptive text |
| NXC | `16` | Data sections in this file |

## Description

  3-Li-  6 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  325
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 45 (a,npa) reaction
    Sum of MT=22, 28, 91 of JENDL/AN-2005 /2/.

  MT=50-53 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 45 (a,npa) reaction
    Calculated with the CCONE code /1/.

  MT=50-53 (a,n') reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
    The neutron emission reaction channels for incident alpha
    particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
    (a,n)       -3.974                 6.621
    (a,pn)      -3.791                 6.313
    (a,a'n)     -5.664                 9.433

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Mehta et al./1/ measured a relative excitation function at
    forward angle (0+/-15deg.). They also measured angular dstri-
    butions of neutrons at Ea=10,12 and 14 MeV. The angular dist-
    ributions were well reproduced by calculation with a modified
    EXIFON code (named "mEXIFON")/2/ using Kalbach's systematics
    /3/ assuming the (a,n) reaction is caused by the multistep
    compound process and the (a,pn) reaction is by multistep
    direct process. Presumably the ground state of Li-6 has large
    component of He-4+deuteron, and the deuteron dissociate into
    n+p by direct recoil caused by incident alpha particle.
    The experimental forward angle excitation function was con-
    verted to the angle integrated excitation function using the
    calculated angular distributions. The absolute cross section
    was determined to reproduce the experimental thick target
    neutron yield measured by Bair and Gomez del Campo/4/. Thick
    target neutron yield was calculated using alpha particle stop-
    ping power given by Ziegler/5/.

 MT=4, 22, 28   (a,n), (a,a'n), (a,pn)
    The ratio of each cross section of neutron emission to
    neutron production cross section was calculated with the mEXI-
    FON code and each cross section was calculated by multiplying
    the ratio to the evaluated neutron production cross section.

 MT=50, 51, 52, 53, 91  (a,n0), (a,n1), (a,n2), (a,n3), (a,nc)
    The ratios of partial (a,ni) cross section to (a,n) cross
    section were calculated with a statistical model code of
    Hauser-Feshbach type and partial cross sections were obtained
    by multiplying the ratio to the evaluated (a,n) cross section
    for the following levels of B-9.

             Level     Ex(MeV)   Spin-Parity
              GS       0.0          3/2-
              1st      1.6          1/2+
              2nd      2.361        5/2-
              3rd      2.788        5/2+

        The levels above 4.8 MeV are assumed to be continuum.

MF=6   Neutron Energy-angle Distributions (law=1, lang=2)
 MT=4, 22, 28
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios of Kalbach's systematics are also given.

References
/1/M.K.Mehta,W.E.Hunt,H.S.Plendl,R.H.Davis:Nucl.Phys.48,90(1963)
/2/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/3/C.Kalbach:Phys.Rev.C37,2350(1988)
/4/J.K.Bair,J.Gomez del Campo:Nucl.Sci.Eng.71,18(1979)
/5/J.F.Ziegler:"Helium:stopping powers and ranges in all
   elements", Pergamon Press,1977




## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 149 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 14 | Original |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 14 | Original |
| 3 | 45 | Cross sections: (α,npα) reaction | 26 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 31 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 22 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 18 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 16 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 33 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 967 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 35,016 | Original |
| 6 | 45 | Energy-angle distributions: (α,npα) reaction | 734 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 50 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 36 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 27 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 24 | Supplement |

---

# Li-7  (Z=3, A=7)
**File:** `a_003-Li-007.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `3007` | Target nucleus: Li-7 |
| AWR | `6.95573` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `141` | Lines of descriptive text |
| NXC | `21` | Data sections in this file |

## Description

  3-Li-  7 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  328
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       -2.790                 4.381
   (a,a'n)     -7.250                11.386

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Gibbons and Macklin/1/ measured the (a,n) reaction cross
    section in the incident alpha particle energy Ea below 8.2MeV.
    The (a,n) partial cross sections were measured by Van der Zwan
    and Geiger/2/ in Ea=4.5-8.0MeV. Mehta et al./3/ measured the
    differential cross section of neutron production in the energy
    range Ea= threshold-15MeV at forward angle(0+/-15deg.). The
    measured cross sections and differential cross sections show
    many resonance structures and analyzed with an approximated
    R-matrix formula/4/. The calculated cross section was adjusted
    to reproduce the thick target neutron yields measured by Bair
    and Gomez del Campo/5/.Thick target neutron yield was calcul-
    ated using alpha particle stopping power given by Ziegler/6/.

 MT=4, 22 (a,n), (a,a'n)
    The ratio of each cross section of neutron emission to neut-
    ron production cross section  was calculated with a modified
    EXIFON code(named "mEXIFON")/7/ and each cross section was
    calculated by multiplying the ratio to the evaluated neutron
    production cross section. Cross sections of the (a,pn) and
    (a,dn) reactions are calculated to be very small and
    neglected in the present file.

 MT=50-54, 91 (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The ratios of partial (a,ni) cross section to (a,n) cross
    section were calculated with a statistical model code of
    Hauser-Feshbach type and partial cross sections were obtained
    by multiplying the ratio to the evaluated (a,n) cross section
    for the following levels of B-10.

             Level     Ex(MeV)   Spin-Parity
              GS       0.0           3 +
              1st      0.718         1 +
              2nd      1.740         0 +
              3rd      2.154         1 +
              4th      3.587         2 +

        The levels above 4.774 MeV are assumed to be continuum.

MF=6     Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 22
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So, it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct re-
    action ratios for Kalbach's systematics/8/ are also given.

References
/1/J.H.Gibbons,R.L.Macklin:Phys.Rev.114,571(1959)
/2/L.Van der Zwan,K.W.Geiger:Nucl.Phys.A180,615(1972)
/3/M.K.Mehta,W.E.Hunt,H.S.Plendl,R.H.Davis:Nucl.Phys.48,90(1963)
/4/T.Murata:JAERI-Conf 98-003,p.215
/5/J.K.Bair,J.Gomez del Campo:Nucl.Sci.Eng.71,18(1979)
/6/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/7/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/8/C.Kalbach:Phys.Rev.C37,2350(1988)




## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 166 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 14 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 65 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 14 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 11 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 63 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 56 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 47 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 44 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 31 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 21 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 65 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 967 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 35,746 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 141 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 67 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 53 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 53 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 41 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 31 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 147 | Supplement |

---

# Be-9  (Z=4, A=9)
**File:** `a_004-Be-009.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `4009` | Target nucleus: Be-9 |
| AWR | `8.93476` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `269` | Lines of descriptive text |
| NXC | `17` | Data sections in this file |

## Description

  4-Be-  9 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  425
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=  4 (a,n') reaction
    Obtained by subtracting MT=22 from MT=201.

  MT= 50, 51, 52, 91 (a,n') reaction
    Obtained by multiplying MT=4 by the MT=50/MT=4, MT=51/MT=4,
    MT=52/MT=4, and MT=91/MT=4 ratios of JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Obtained by multiplying MT=201 of JENDL-2005 /2/ by the
    experimental MT=22/MT=201 ratios reported by Gieger et al. /3/

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 50-52 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)
 3) K.W.Gieger et al., NRCC-15303 (1976)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Revised by T.Murata(AITEL) and K.Shibata(JAERI)
------- Modifications for AN-2005 --------------------------------
mf/mt=1/451         modified
mf/mt=3/4           sum of 3/50-52,91
mf/mt=3/50-52,3/91  modified
mf/mt=3/53-54       deleted
mf/mt=3/201         sum of 3/4 and 3/22
mf/mt=6/4           deleted
mf/mt=6/22          modified
mf/mt=6/50-52,91    newly added

       * Comments for the previous evaluation  *

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       +5.701                  0.0
   (a,a'n)     -1.665                  2.405

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Gibbons and Macklin/1/ measured neutron production cross
    section in the energy range Ea=1.66-10.3MeV. In the low energy
    region Ea=0.15-1.86MeV,Wrean et al./2/ measured the cross sec-
    tion with fine energy step. Van der Zwan and Geiger/3/ measur-
    ed the (a,n0),(a,n1) and (a,n2) cross sections in some energy
    region in Ea=1.6-7.9MeV. Results of Gibbons-Macklin agree well
    with that of Wrean et al. Sum of partial cross sections meas-
    ured by Van der Zwan-Geiger gives not so good agreement. Reso-
    nance analysis was made for the cross sections of Gibbons-
    Macklin and Wrean et al. with an approximated R-matrix formula
    /4/. The data of Van der Zwan and Geiger were adopted as rela-
    tive ratio data for partial cross sections. The (a,a'n) cross
    section was measured by Obst et al./5/. Calculated (a,a'n)
    cross section with a modified EXIFON code(named "mEXIFON")/6/
    was normalized to the experimental cross section, and used for
    the resonance analysis as background cross section. The fitted
    cross section was adjusted to reproduce the experimental thick
    target neutron yields measured by Bair-Gomez del Campo/7/ and
    West-Sherwood/8/ using alpha particle stopping power given by
    Ziegler/9/.

 MT=4, 22   (a,n), (a,a'n)
    The (a,a'n) cross section was obtained as described in the
    preceding section. The (a,pn) cross section calculated with
    the mEXIFON code is very small and neglected in the present
    evaluation.

 MT=50-54, 91 (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The (a,n0),(a,n1) and (a,n2) cross sections in Ea<7.9 MeV,
    resonance anlysis was made consistently with the neutron prod-
    uction cross section. In the higher energy region, the (a,n0)
    cross section was determined using inverse reaction C12(n,a0)
    Be9 cross section of JENDL-3.2/10/. Other partial cross sect-
    ions were obtained by ratio calculation with a statistical
    model of Hauser-Feshbach type.
    The level scheme of C-12 for the present calculation is
    given in the following table.

             Level     Ex(MeV)   Spin-Parity
              GS       0.0           0 +
              1st      4.439         2 +
              2nd      7.654         0 +
              3rd      9.641         3 -
              4th     10.3           0 +
         The levels above 10.844 MeV are assumed to be continuum.

MF=6     Neutron Energy-Angle Distributions(LAW=1,Lang=2)
  MT=4, 22
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So, it
    will give better results, on an average, to adopt statistical
    model for the calculation of of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/11/ are also given.


References
/1/J.H.Gibbons,R.L.Macklin:Phys.Rev.B137,1508(1965)
/2/P.R.Wrean,C.R.Brune,R.W.Kavanagh:Phys.Rev.C49,1205(1994)
/3/L.Van der Zwan,K.W.Geiger:Nucl.Phys.A152,481(1970)
/4/T.Murata:JAERI-Conf 98-003,p.215
/5/A.W.Obst,T.B.Grandy,J.L.Weil:Phys.Rev.C5,738,(1972)
/6/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/7/J.K.Bair,J.Gomez del Campo:Nucl.Sci.Eng.71,18(1979)
/8/D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/9/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/10/K.Shibata: JAERI-M 83-221 (1983)
/11/C.Kalbach:Phys.Rev.C37,2350(1988)

       * Comments for the present evaluation (AN-2005) *

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       +5.701                  0.0
   (a,a'n)     -1.665                  2.405


MF=3   Cross Sections
 Neutron Production Cross Section
      Gibbons and Macklin/1/ measured neutron production cross
    section in the energy range Ea=1.66-10.3MeV. In the low energy
    region Ea=0.15-1.86MeV,Wrean et al./2/ measured the cross sec-
    tion with fine energy step. Van der Zwan and Geiger/3/ measur-
    ed the (a,n0),(a,n1) and (a,n2) cross sections in some energy
    region in Ea=1.6-7.9MeV. Results of Gibbons-Macklin agree well
    with that of Wrean et al. Sum of partial cross sections meas-
    ured by Van der Zwan-Geiger gives not so good agreement. Reso-
    nance analysis was made for the cross sections of Gibbons-
    Macklin and Wrean et al. with an approximated R-matrix formula
    /4/. The data of Van der Zwan and Geiger were adopted as rela-
    tive ratio data for partial cross sections. The (a,a'n) cross
    section was measured by Obst et al./5/. Calculated (a,a'n)
    cross section with a modified EXIFON code(named "mEXIFON")/6/
    was normalized to the experimental cross section, and used for
    the resonance analysis as background cross section. The fitted
    cross section was adjusted to reproduce the experimental thick
    target neutron yields measured by Bair-Gomez del Campo/7/ and
    West-Sherwood/8/ using alpha particle stopping power given by
    Ziegler/9/.

 MT=4 (a,n)
      Sum of MT=50-52, 91
 MT=22 (a,a'n)
      The (a,a'n) cross section was obtained as described in the
    preceding section. The (a,pn) cross section calculated with
    the mEXIFON code is fairly small and neglected in the present
    evaluation.
 MT=50 (a,n0),MT=51 (a,n1),MT=52 (a,n2), MT=91 (a,nc)
      The (a,n0),(a,n1) and (a,n2) cross sections in Ea<7.9 MeV,
    resonance anlysis was made consistently with the neutron prod-
    uction cross section. In the higher energy region, the (a,n0)
    cross section was determined using inverse reaction C12(n,a0)
    Be9 cross section of JENDL-3.2/10/. Other partial cross sect-
    ions were obtained by ratio calculation with a statistical
    model of Hauser-Feshbach type.
      The level scheme of C-12 for the present calculation is
    given in the following table.

             Level     Ex(MeV)   Spin-Parity
              GS       0.0           0 +
              1st      4.439         2 +
              2nd      7.654         0 +
              3rd      9.641         3 -
              4th     10.3           0 +
              5th     10.844         1 -
         The levels above 9.641 MeV are assumed to be continuum.

MF=6
  MT=50 (a,n0),MT=51 (a,n1),MT=52 (a,n2),MT=91 (a,nc),
  MT=22 (a,a'n)
  Neutron Energy-Angle Distributions
       Angular distributions of neutrons to the ground,1st and 2nd
    excited states of C-12 were measured by Obst et al./5/ in the
    incident energy range 3.21MeV to 6.44MeV. In this energy range
    experimental angular distributions were converted to the cen-
    ter of mass system and fitted with Legendre polynomials. Eval-
    uation of the coefficients of the polynomials were made on the
    experimental values in the this range, while in the other ene-
    rgy range, we adopted the results of the Blatt-Biedenharn type
    calculations using the resonance parameters determined in the
    cross-section analysis.
       For neutron energy-angle distribution by the (a,nc) and
    (a,a'n) reactions, calculations were made with mEXIFON code
    and given in Kalbach's systematics/11/ (LAW=1,Lang=2).


References
/1/J.H.Gibbons,R.L.Macklin:Phys.Rev.B137,1508(1965)
/2/P.R.Wrean,C.R.Brune,R.W.Kavanagh:Phys.Rev.C49,1205(1994)
/3/L.Van der Zwan,K.W.Geiger:Nucl.Phys.A152,481(1970)
/4/T.Murata:JAERI-Conf 98-003,p.215
/5/A.W.Obst,T.B.Grandy,J.L.Weil:Phys.Rev.C5,738,(1972)
/6/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/7/J.K.Bair,J.Gomez del Campo:Nucl.Sci.Eng.71,18(1979)
/8/D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/9/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/10/K.Shibata:JAERI-M 84-226(1984)
/11/C.Kalbach:Phys.Rev.C37,2350(1988)


## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 290 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 17 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 231 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 17 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 195 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 231 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 211 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 188 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 118 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 231 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,277 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 24,633 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 1,300 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 150 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 138 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 117 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 662 | Supplement |

---

# B-10  (Z=5, A=10)
**File:** `a_005-B-010.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `5010` | Target nucleus: B-10 |
| AWR | `9.92692` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `157` | Lines of descriptive text |
| NXC | `23` | Data sections in this file |

## Description

  5-B - 10 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  525
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 28 (a,np) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Proton  component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       +1.059                  0.0
   (a,pn)      -0.885                  1.238
   (a,a'n)     -8.436                 11.809

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Gibbons and Macklin/1/ measured neutron production cross
    section in the incident energy range Ea=2.55-4.83MeV. Van der
    Zwan and Geiger/2/ measured the (a,n0),(a,n1) and (a,n2+n3)
    differential cross sections at 2 or 3 angles in the energy
    range Ea=1.0-5.0MeV. Resonance analysis was made for the cross
    sections of Gibbons and Macklin and for the 90 degree (a,n0)
    differential cross section x 4pi of Van der Zwan and Geiger in
    Ea<2.6MeV. The analysis was made with an approximated R-matrix
    formula/3/. The fitted cross section was reduced by about fac-
    tor 0.4 to reproduce the experimental thick target neutron
    yields measured by Bair and Gomez del Campo/4/ using alpha
    particle stopping power given by Ziegler/5/. The reason of
    this discrepancy between the experimental thick target neutron
    yield and experimental cross section based calculated yield is
    not clear. In the energy region Ea>5MeV,the cross section was
    calculated with a modified EXIFON code(named "mEXIFON")/6/ and
    normalized to the cross section in Ea<=5MeV.

 MT=4, 22, 28   (a,n), (a,a'n), (a,pn)
    The ratio of each cross section of neutron emission to neut-
    ron production cross section was calculated with the mEXIFON
    code and each cross section was calculated by multiplying the
    ratio to the evaluated neutron production cross section.

 MT=50-54, 91 (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The ratios of partial (a,ni) cross section to (a,n) cross
    section were calculated with Hauser-Feshbach type statistical
    model and partial cross sections were obtained by multiplying
    the ratio to the evaluated (a,n) cross section for the follow-
    ing levels of N-13.

                       Ex(MeV)   Spin-Parity
              GS       0.0          1/2-
              1st      2.365        1/2+
              2nd      3.511        3/2-
              3rd      3.547        5/2+
              4th      6.364        5/2+
           The levels above 6.885 MeV are assumed to be continuum.

    Roughton et al./7/ measured thick target N-13 activity yield
    in the energy range Ea=3.2-14.2MeV. Above the 1st excited
    state, N-13 almost decays to C-12 by proton emission,so,the
    activity production cross section is almost equal to the
    (a,n0) cross section. Calculated cross section was adjusted to
    reproduce the thick target N-13 activity yield.

MF=6    Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 22, 28
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So,it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/8/ are also given.

References
/1/J.H.Gibbons,R.L.Macklin:Phys.Rev.114,571(1959)
/2/L.Van der Zwan,K.W.Geiger:Nucl.Phys.A216,188(1973)
/3/T.Murata:JAERI-Conf 98-003,p.215
/4/J.K.Bair,J.Gomez del Campo:Nucl.Sci.Eng.71,18(1979)
/5/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/6/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/7/N.A.Roughton,T.P.Intrator,R.J.Peterson,C.Z.Zaidins,C.J.Hansen:
   Atomic Data and Nuclear Data Tables,28,341(1983)
/8/C.Kalbach:Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 184 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 21 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 56 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 21 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 5 | Supplement |
| 3 | 28 | Cross sections: (α,pn) reaction | 42 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 54 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 47 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 32 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 32 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 16 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 15 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 56 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,680 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 105,582 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 114 | Supplement |
| 6 | 28 | Energy-angle distributions: (α,pn) reaction | 1,092 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 170 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 151 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 134 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 138 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 96 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 402 | Supplement |

---

# B-11  (Z=5, A=11)
**File:** `a_005-B-011.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `5011` | Target nucleus: B-11 |
| AWR | `10.91473` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `149` | Lines of descriptive text |
| NXC | `23` | Data sections in this file |

## Description

  5-B - 11 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  528
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 16 (a,2n) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 16 (a,2n) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Proton  component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       +0.158                  0.0
   (a,pn)      -7.392                 10.080
   (a,2n)     -10.395                 14.175

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Van der Zwan and Geiger/1/ measured the (a,n0),(a,n1) and
    (a,n2) cross sections and angular distributions in the energy
    range Ea=3.7-7.9. The (a,n0) cross section in the whole energy
    range was obtained from the inverse reaction N14(n,a0)B11
    cross section of JENDL-3.2 /2/. Resonance analysis was made
    for the cross sections of (a,n0) reaction with an approximated
    R-matrix formula/3/. Thus obtained (a,n0) cross section was
    converted to neutron production cross section by multiplying
    energy dependent factor which determined to reproduce the exp-
    erimental thick target neutron yield measured by Bair and
    Gomez del Campo/4/ in the energy range Ea=3.5-7.5MeV. Calcula-
    tion of thick target neutron yield was made using alpha parti-
    cle stopping power given by Ziegler/5/. In the energy region
    Ea>7.5MeV, the neutron production cross section was calculated
    with a modified EXIFON code(named "mEXIFON")/6/, and normal-
    ized to the neutron production cross section in Ea<=7.5MeV.

 MT=4, 16, 28   (a,n), (a,2n), (a,pn)
    The ratio of each cross section of neutron emission to
    neutron production cross section was calculated with mEXIFON
    code, and each cross section was calculated by multiplying the
    ratio to the evaluated neutron production cross section. The
    (a,dn) cross section was calculated to be very small and
    ignored in the present evaluation.

 MT=50-54,91  (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The (a,n0) cross section was determined as described in the
    preceding section. Other partial cross sections were calculat-
    ed by ratio of each cross section to the neutron production
    minus (a,n0) cross section. The ratio was calculated with a
    statistical model code of Hauser-Feshbach type for the follow-
    ing levels of N-14,including T-spin factor.

                       Ex(MeV)   Spin-Parity   T-spin
              GS       0.0           1 +         0
              1st      2.313         0 +         1
              2nd      3.948         1 +         0
              3rd      4.915         0 -         0
              4th      5.106         2 -         0
           The levels above 5.690 MeV are assumed to be continuum.

MF=6   Neutron Energy-Angle Distributions (LAW=1, LANG=2)
 MT=4, 16, 28
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So, it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/7/ are also given.

References
/1/L.Van der Zwan,K.W.Geiger:Nucl.Phys.A246,93(1975)
/2/K.Shibata et al.:JAERI 1319 (1990)
/3/T.Murata:JAERI-Conf 98-003,p.215
/4/J.K.Bair,J.Gomez del Campo:Nucl.Sci.Eng.71,18(1979)
/5/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/6/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/7/C.Kalbach:Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 176 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 19 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 232 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 19 | Original |
| 3 | 16 | Cross sections: MT=16 | 5 | Supplement |
| 3 | 28 | Cross sections: (α,pn) reaction | 30 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 231 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 165 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 91 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 60 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 59 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 53 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 233 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,494 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 81,207 | Original |
| 6 | 16 | Energy-angle distributions: MT=16 | 21 | Supplement |
| 6 | 28 | Energy-angle distributions: (α,pn) reaction | 238 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 148 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 129 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 113 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 107 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 93 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 389 | Supplement |

---

# C-12  (Z=6, A=12)
**File:** `a_006-C-012.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `6012` | Target nucleus: C-12 |
| AWR | `11.89691` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `105` | Lines of descriptive text |
| NXC | `9` | Data sections in this file |

## Description

  6-C - 12 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  625
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 50 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       -8.502                11.338

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Black et al./1/ measured O-15 production cross section in
    the incident alpha particle energy range Ea=threshold-22.65
    MeV. Only one reaction channel (a.n0) is open for neutron
    emission in Ea<=15MeV. Resonance analysis was made for the
    cross section of Black et al. with an approximated R-matrix
    formula/2/.
    Natural carbon thick target neutron yields were measured by
    Bair/3/ in Ea=2-9MeV and by West and Sherwood/4/ in Ea=3.6-10
    MeV. Using the present C-12 and C13 neutron production cross
    sections,the thick target neutron yield was calculated and
    compared with the experimental data. The calculation was made
    with alpha particle stopping power given by Ziegler/5/. Then
    small adjustment was made for the cross sections.
 MT=4 (a,n)
    Equal to MT=50.
 MT=50 (a,n0)
    Only the (a,n0) reaction channel is open, so, the evaluated
    neutron production cross section is equal to the (a,n0) cross
    section.

MF=6 Angular Distributions of Secondary Neutrons
 MT=50 (a,n0)
    Neutron energy spectrum are consist of that of the (a,n0)
    reaction only. Angular distributions are given by Legendre
    expansion coefficients which were calculated with Blatt-
    Biedenharn formula/6/ using the resonance parameters obtained
    in the above analysis.

References
/1/ J.L.Black,H.M.Kuan,W.Gruhle,M.Suffert,G.L.Latshaw:Nucl.Phys.
    115,683(1968)
/2/T.Murata:JAERI-Conf 98-003,p.215
/3/J.K.Bair:Nucl.Sci.Eng.51,83(1973)
/4/D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/5/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/6/P.M.Endt,M.Demeur(editers):"Nuclear Reactions",vol.1,chapt.V,
   "Resonance Reactions,Theoretical" by E.Vogt,North-Holland,1959



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 118 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 15 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 53 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 15 | Original |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 53 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 53 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,122 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 25,549 | Original |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 284 | Supplement |

---

# C-13  (Z=6, A=13)
**File:** `a_006-C-013.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `6013` | Target nucleus: C-13 |
| AWR | `12.89165` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `150` | Lines of descriptive text |
| NXC | `23` | Data sections in this file |

## Description

  6-C - 13 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  628
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 28 (a,np) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Proton  component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)        +2.216                 0.0
   (a,pn)       -9.912                12.963
   (a,a'n)      -4.946                 6.469

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Sekharan et al./1/ measured neutron production cross section
    in the energy range Ea=1.9-5.6MeV. Bair and Haas/2/ measured
    the cross section in Ea=1.0-5.4MeV. Resonance analysis was
    made for these cross sections with an approximated R-matrix
    formula/3/. Above Ea=5.6MeV, neutron production cross section
    was calculated with a modified EXIFON code (named "mEXIFON")
    /4/,and normalized to the cross section below Ea=5.6MeV.
    Natural carbon thick target neutron yields were measured by
    Bair/5/ in Ea=2-9MeV and by West and Sherwood/6/ in Ea=3.6-10
    MeV. Using the present C-12 and C13 neutron production cross
    sections,the thick target neutron yield was calculated and
    compared with the experimental data. The calculation was made
    with alpha particle stopping power given by Ziegler/7/. Then
    small adjustment was made for the cross sections.

 MT=4, 22, 28 (a,n), (a,a'n), (a,pn)
    The ratio of each cross section of neutron emission to neut-
    ron production cross section  was calculated with the mEXIFON
    code, and each cross section was calculated by multiplying the
    ratio to the evaluated neutron production cross section.

 MT=51-54, 91 (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The (a,n0) cross section,in the whole energy region, was
    obtained from the inverse reaction O16(n,a0)C13 cross section
    given in ENDF/B-6 /8/. Other partial cross sections were
    obtained by ratio calculation with a statistical model code of
    Hauser-Feshbach type. The level scheme of O-16 for the present
    calculation is given in the following table.

                       Ex(MeV)   Spin-Parity
              GS       0.0           0 +
              1st      6.049         0 +
              2nd      6.130         3 -
              3rd      6.917         2 +
              4th      7.117         1 -
           The levels above 8.872 MeV are assumed to be continuum.

MF=6   Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 22, 28
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So,it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/9/ are also given.

References
/1/K.K.Sekharan,A.S.Divatia,M.K.Metha,S.S.Kerekatte,K.B.Nambiar:
   Phys.Rev.156,1187(1967)
/2/J.K.Bair,F.X.Haas:Phys.Rev.C7,1356,(1973)
/3/T.Murata:JAERI-Conf 98-003,p.215
/4/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/5/J.K.Bair:Nucl.Sci.Eng.51,83(1979)
/6/D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/7/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/8/G.M.Hale,P.G.Young,M.Chadwick,Z.-P.Chen:Proc.Int.Conf.Nuclear
   Data forScience and Technology,Julich,13-17,May 1991,p.921
/9/C.Kalbach:Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 177 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 19 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 285 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 19 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 15 | Supplement |
| 3 | 28 | Cross sections: (α,pn) reaction | 6 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 284 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 58 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 52 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 19 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 18 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 14 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 286 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,432 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 35,803 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 518 | Supplement |
| 6 | 28 | Energy-angle distributions: (α,pn) reaction | 72 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 170 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 110 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 102 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 98 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 97 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 448 | Supplement |

---

# N-14  (Z=7, A=14)
**File:** `a_007-N-014.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `7014` | Target nucleus: N-14 |
| AWR | `13.88278` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `151` | Lines of descriptive text |
| NXC | `23` | Data sections in this file |

## Description

  7-N - 14 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  725
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 28 (a,np) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Proton  component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)        -4.734                 6.088
   (a,pn)       -5.335                 6.860
   (a,a'n)     -10.553                13.570

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Gruhle et al./1/ measured F-17 activity production cross
    section in the incident alpha particle energy range Ea=6-19.8
    MeV. The excited states of F-17 of which excited energy great-
    er than 0.6MeV, decay to O16+p state. So, the F-17 activity
    production cross section almost equal to the (a,n0)+(a,n1)
    cross section. Resonance analysis was made for the cross sect-
    ion with an approximated R-matrix formula/2/.
    Roughton et al./3/ measured thick target F-17 activity
    yield in the energy range Ea=6.2-16.8MeV. Thick target F-17
    yield was calculated using the analyzed cross section with
    alpha particle stopping power given by Ziegler/4/. The experi-
    mental data of Roughton et al. discrepant unnaturally with the
    calculated one at two energy points. Ignoring these points,
    good agreement was obtained. The F-17 production cross section
    was converted to the neutron production cross section using
    the ratio of these cross sections calculated with a modfied
    EXIFON code(named "mEXIFON")/5/.

 MT=4, 22, 28  (a,n), (a,a'n), (a,pn)
    The ratio of each cross section of neutron emission to
    neutron production cross section was calculated with the
    mEXIFON code, and each cross section was calculated by multi-
    plying the ratio to the evaluated neutron production cross
    section.

 MT=50-54, 91  (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The (a,n0) and (a,n1) cross sections were obtained from the
    F-17 production cross section, deviding it with the ratio
    calculated with a statistical model code of Hauser-Feshbach
    type. Other cross sections were obtained by ratio calculation
    with the same code. The level scheme of F-17 for the present
    calculation is given in the following table.

                       Ex(MeV)   Spin-Parity
              GS       0.0          5/2+
              1st      0.495        1/2+
              2nd      3.104        1/2-
              3rd      3.857        5/2-
              4th      4.640        3/2-
           The levels above 5.000 MeV are assumed to be continuum.

MF=6   Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 22, 28
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So,it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/6/ are also given.


Reference
/1/W.Gruhle, W.Schmidt, W.Burgmer: Nucl. Phys.,A186,257 (1972)
/2/T.Murata:JAERI-Conf 98-003,p.215
/3/N.A.Roughton, T.P.Intrator, R.J.Peterson, C.S.Zaidins,
   C.J.Hansen: Atomic Data and Nuclear Data Tables  28, 341(1983)
/4/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/5/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/6/C.Kalbach:Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 178 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 25 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 105 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 25 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 6 | Supplement |
| 3 | 28 | Cross sections: (α,pn) reaction | 81 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 103 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 95 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 57 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 46 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 35 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 30 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 106 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 2,052 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 100,531 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 53 | Supplement |
| 6 | 28 | Energy-angle distributions: (α,pn) reaction | 508 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 150 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 147 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 103 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 91 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 66 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 118 | Supplement |

---

# N-15  (Z=7, A=15)
**File:** `a_007-N-015.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `7015` | Target nucleus: N-15 |
| AWR | `14.87125` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `140` | Lines of descriptive text |
| NXC | `21` | Data sections in this file |

## Description

  7-N - 15 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  728
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)        -6.418                 8.131
   (a,a'n)     -10.833                13.572

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    No experimental cross section was available. Resonance
    levels of the compound nucleus F-19 were selected to meet the
    condition of alpha particle and neutron emission from the
    level scheme of F-19 /1/. Using the resonance parameters of
    the selected 17 resonances,the cross section was calculated
    with an approximated R-matrix formula/2/.
    Roughton et al./3/ measured thick target F-18 activity yield
    in the incident alpha particle energy Ea=8.4-16.8MeV. The
    activation cross section corresponds approximately to the sum
    of (a,ni) cross sections to the F-18 excited levels of which
    excitation energy less than particle emission energy;Ex<=4.416
    MeV. The calculated cross section was adjusted to reproduce
    the experimrntal thick target F-18 yield. Thick target yield
    calculation was made using alpha particle stopping power given
    by Ziegler/4/.

 MT=4, 22  (a,n), (a,a'n)
    The ratio of each cross section of neutron emission to the
    neutron production cross section was calculated with a modif-
    ied EXIFON code(named "mEXIFON")/5/, and each cross section
    was calculated by multiplying the ratio to the evaluated neut-
    ron production cross section.

 MT=50-54, 91 (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The partial cross sections were obtained by ratio calcula-
    tion with a statistical model code of Hauser-Feshbach type
    including T-spin factor. The level scheme of F-18 for the
    present calculation is given in the following table.

                       Ex(MeV)   Spin-Parity    T-spin
              GS       0.0           1 +          0
              1st      0.937         3 +          0
              2nd      1.042         0 +          1
              3rd      1.081         0 -          0
              4th      1.121         5 +          0
           The levels above 1.700 MeV are assumed to be continuum.

MF=6   Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 22
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So,it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
      Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/6/ are also given.


References
/1/D.R.Tilley,H.R.Weller,C.M.Cheves,R.M.Chasteler:
   Nucl. Phys.A595,1 (1995).
/2/T.Murata:JAERI-Conf 98-003,p.215
/3/N.A.Roughton,T.P.Intrator,R.J.Peterson,C.S.Zaidins,C.J.Hansen:
   Atomic Data and Nuclear Data Tables  28, 341(1983).
/4/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/5/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/6/C.Kalbach:Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 165 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 22 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 39 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 22 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 5 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 37 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 30 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 30 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 30 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 30 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 26 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 39 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,742 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 63,305 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 43 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 112 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 100 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 104 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 102 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 92 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 112 | Supplement |

---

# O-16  (Z=8, A=16)
**File:** `a_008-O-016.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `8016` | Target nucleus: O-16 |
| AWR | `15.85751` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `111` | Lines of descriptive text |
| NXC | `5` | Data sections in this file |

## Description

  8-O - 16 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  825
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated with CCONE code by nakayama

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Neutron cross sections
  MT=  2 Elastic scattering cross section
    Calculated with CCONE code /1/.

  MT=  3 Non-elastic cross section
    Calculated with CCONE code /1/.

  MT=  5 Total reaction (except fission) cross section
    Calculated with CCONE code /1/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
    Calculated with CCONE code /1/.

  MT=  5 Total reaction (except fission) reaction
    Calculated with CCONE code /1/.

MF= 8 Information on decay data
  MT=  5 Total reaction (except fission) reaction
    Decay chain is given in the decay data file.

          nuclear model calculation with CCONE code /1/
* Optical model potentials
  neutron : global OMP, A.J.Koning and J.P.Delaroche/2/
  proton  : global OMP, A.J.Koning and J.P.Delaroche/2/
  deuteron: Y.Han et al./3/
  triton  : folding OMP, A.J.Koning and J.P.Delaroche/2/
  He-3    : folding OMP, A.J.Koning and J.P.Delaroche/2/
  alpha   : V.Avrigeanu et al./4/

* Level scheme of O-16
   No.   Ex(MeV)    J PI
    0   0.000000    0 +
    1   6.049400    0 +
    2   6.129890    3 -
    3   6.917100    2 +
    4   7.116850    1 -
    5   8.871900    2 -
    6   9.585000    1 -
    7   9.844500    2 +
    8  10.356000    4 +
    9  10.957000    0 -
   10  11.080000    3 +
   11  11.096700    4 +
   12  11.260000    0 +
   13  11.520000    2 +
   14  11.600000    3 -
   15  12.049000    0 +
   16  12.440000    1 -
   17  12.530000    2 -
   18  12.796000    0 -
   19  12.968600    2 -
   20  13.020000    2 +
   21  13.090000    1 -
   22  13.129000    3 -
   23  13.259000    3 -
   24  13.664000    1 +
   25  13.869000    4 +
   26  13.980000    2 -
   27  14.032000    0 +
   28  14.100000    3 -
   29  14.302000    4 -

* Level density parameters (Gilbert-Cameron model/5/)
  Energy dependent parameters of Mengoni-Nakajima/6/ were used.
          a*     Pair  Eshell   T      E0   Ematch  Elv_max
         1/MeV   MeV    MeV    MeV    MeV     MeV     MeV
  Ne-20   3.685  5.367 -1.756  2.357  3.121  20.347  11.528
  F-19    3.543  2.753  0.484  2.355 -1.166  15.665   8.793
  O-16    3.104  6.000 -5.253  3.138  3.736  34.004  14.302

* Gamma-ray strength functions for Ne-20
  E1: enhanced generalized lorentzian model(EGLO)/7/
    ER= 19.31 (MeV) EG=  7.43 (MeV) SIG=   6.79 (mb)
    ER= 27.31 (MeV) EG= 14.40 (MeV) SIG=  13.58 (mb)
  M1: standard lorentzian model(SLO)
    ER= 15.10 (MeV) EG=  4.00 (MeV) SIG=   2.14 (mb)
  E2: standard lorentzian model(SLO)
    ER= 23.21 (MeV) EG=  5.87 (MeV) SIG=   0.51 (mb)

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) A.J.Koning and J.P.Delaroche, Nucl. Phys. A713, 231 (2003)
 3) Y.Han et al., Phys. Rev. C 74,044615(2006)
 4) V.Avrigeanu et al., Report OUNP-94-02 (1994) , Phys. Rev.
    C49,2136 (1994)
 5) A. Gilbert and A.G.W. Cameron, Can. J. Phys, 43, 1446 (1965)
 6) A. Mengoni and Y. Nakajima, J. Nucl. Sci. Technol., 31, 151
    (1994)
 7) J. Kopecky et al., Phys. Rev. C 47, 312 (1993)


## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 120 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 18 | Original |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 18 | Original |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,370 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 29,487 | Original |

---

# O-17  (Z=8, A=17)
**File:** `a_008-O-017.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `8017` | Target nucleus: O-17 |
| AWR | `16.85310` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `143` | Lines of descriptive text |
| NXC | `19` | Data sections in this file |

## Description

  8-O - 17 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  828
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 50-53 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)        +0.587                 0.0
   (a,a'n)      -4.143                 5.119

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Bair and Haas/1/ measured the neutron production cross
    section in the incident alpha particle energy range Ea=1.0-5.3
    MeV. It was pointed out later/2/ that the results should be
    multiplied by a factor 1.35. Hansen et al./3/ measured the
    neutron production cross section in the energy range Ea= 5-
    12.5 MeV with broad incident energy resolution. Resonance
    analysis was made for the revised cross section of Bair and
    Haas with an approximated R-matrix formula/4/. Above Ea=5.3
    MeV, neutron production cross section was calculated with a
    modified EXIFON code (named "mEXIFON")/5/, and normalized to
    the cross section below Ea=5.3MeV and that of Hansen et al.
    Thick UO2(natural oxygen) target neutron yield was measured
    by Bair and Gomez del Campo/2/ in Ea=3.0-7.5MeV and by West
    and Sherwood/6/ in Ea=3.8-10MeV. Thick UO2(natural oxygen)
    target neutron yield was calculated with the present O-17 and
    O-18 neutron production cross sections using alpha particle
    stopping power given by Ziegler/7/, and compared with the exp-
    erimental yield, small adjustment was made for the cross sect-
    ion.

 MT=4, 22 (a,n), (a,a'n)
    The ratio of each cross section of neutron emission to neut-
    ron production cross section was calculated with the mEXIFON
    code, and each cross section was calculated by multiplying the
    ratio to the evaluated neutron production cross section.

 MT=50-53, 91  (a,n0), (a,n1), (a,n2), (a,n3), (a,nc)
    The partial cross sections were obtained by ratio calcula-
    tion with a statistical model code of Hauser-Feshbach type.
    The level scheme of Ne-20 for the present calculation is given
    in the following table.

                       Ex(MeV)   Spin-Parity
              GS       0.0           0 +
              1st      1.634         2 +
              2nd      4.248         4 +
              3rd      4.968         2 -

           The levels above 5.621 MeV are assumed to be continuum.

MF=6    Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 22
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So,it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/8/ are also given.

References
/1/J.K.Bair, F.X.Haas: Phys.Rev.156,1187(1967)
/2/J.K.Bair,J.Gomez del Campo: Nucl.Sci.Eng.,71,18(1979)
/3/L.F.Hansen, J.D.Anderson, J.W.McClure, B.A.Pohl, M.L.Stelts,
   J.J.Wesolowski, C.Wong: Nucl. Phys.,A198,25(1967).
/4/T.Murata:JAERI-Conf 98-003,p.215
/5/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/6/D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/7/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/8/C.Kalbach:Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 166 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 27 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 138 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 27 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 17 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 137 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 136 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 43 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 20 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 18 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 138 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 2,176 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 56,258 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 1,126 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 240 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 212 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 168 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 166 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 495 | Supplement |

---

# O-18  (Z=8, A=18)
**File:** `a_008-O-018.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `8018` | Target nucleus: O-18 |
| AWR | `17.84454` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `149` | Lines of descriptive text |
| NXC | `23` | Data sections in this file |

## Description

  8-O - 18 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  831
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 16 (a,2n) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 16 (a,2n) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Neutron component : taken from JENDL/AN-2005 /2/.
    Alpha   component : calculated with the CCONE code /1/.

  MT= 50-54 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Taken from MF6/MT4 of JENDL/AN-2005 /2/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-09 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)         -0.697                 0.852
   (a,a'n)       -8.044                 9.833
   (a,2n)        -7.458                 9.116

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
    Bair and Willard/1/ measured the neutron production cross
    section in the energy range Ea=2.4-5.1MeV.It was pointed out
    later/2/ that the results should be multiplied by a factor
    1.35. Hansen et al./3/ measured the neutron production cross
    section in the energy range Ea= 5-12.5 MeV with broad incident
    energy resolution. Resonance analysis was made for the revised
    cross section of Bair and Willard with an approximated R-mat-
    rix formula/4/. Above Ea=5.1MeV, neutron production cross
    section was calculated with a modified EXIFON code (named
    "mEXIFON")/5/, and normalized to the cross section below
    Ea=5.1 MeV and that of Hansen et al.
    Thick UO2(natural oxygen) target neutron yield was measured
    by Bair and Gomez del Campo/2/ in Ea=3.0-7.5MeV and by West
    and Sherwood/6/ in Ea=3.8-10MeV. Thick UO2(natural oxygen)
    target neutron yield was calculated with the present O-17 and
    O-18 neutron production cross sections using alpha particle
    stopping power given by Ziegler/7/, and compared with the exp-
    erimental yield, small adjustment was made for the cross sect-
    ion.

 MT=4, 16, 22  (a,n), (a,2n), (a,a'n)
    The ratio of each cross section of neutron emission to neut-
    ron production cross section was calculated with the mEXIFON
    code, and each cross section was calculated by multiplying the
    ratio to the evaluated neutron production cross section.

 MT=50-54, 91 (a,n0), (a,n1), (a,n2), (a,n3), (a,n4), (a,nc)
    The partial cross sections were obtained by ratio calcul-
    ation with a statistical model code of Hauser-Feshbach type.
    The level scheme of Ne-21 for the present calculation is given
    in the following table.

                       Ex(MeV)   Spin-Parity
              GS       0.0          3/2+
              1st      0.351        5/2+
              2nd      1.746        7/2+
              3rd      2.789        1/2-
              4th      2.794        1/2+
           The levels above 2.867 MeV are assumed to be continuum.

MF=6  Neutron Energy-Angle Distributions(LAW=1,Lang=2)
 MT=4, 16, 22
    Though the angular distribution and energy spectrum of the
    emitted neutrons can be calculated with the determined resona-
    nce parameters, there is ambiguity of spin-parity of resonance
    levels determined by an analysis of the (a,n) channel only,
    and these quantities depend on spin-parity strongly. So,it
    will give better results, on an average, to adopt statistical
    model for the calculation of energy-angle distributions.
    Emitted neutron contineous energy spectrum were calculated
    with the mEXIFON code for each reaction. Multistep direct
    reaction ratios for Kalbach's systematics/8/ are also given.


References
/1/J.K.Bair,H.B.Willard: Phys.Rev.128,299(1962).
/2/J.K.Bair,J.Gomez del Campo: Nucl.Sci.Eng.,71,18(1979)
/3/L.F.Hansen, J.D.Anderson, J.W.McClure, B.A.Pohl, M.L.Stelts,
   J.J.Wesolowski, C.Wong: Nucl. Phys.,A198,25(1967).
/4/T.Murata:JAERI-Conf 98-003,p.215
/5/T.Murata:JAERI-Conf 97-005,p.286
   original EXIFON code developed by H.Kalka:Z.Phys.A341,289(1992)
/6/D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/7/J.F.Ziegler:"Helium:stopping powers and ranges in all elements"
   Pergamon Press,1977
/8/C.Kalbach:Phys.Rev.C37,2350(1988)

## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 176 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 24 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 120 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 24 | Original |
| 3 | 16 | Cross sections: MT=16 | 13 | Supplement |
| 3 | 22 | Cross sections: (α,nα) reaction | 9 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 119 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 119 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 86 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 45 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 45 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 39 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 121 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,959 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 49,182 | Original |
| 6 | 16 | Energy-angle distributions: MT=16 | 109 | Supplement |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 285 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 200 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 197 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 174 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 167 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 171 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 470 | Supplement |

---

# F-19  (Z=9, A=19)
**File:** `a_009-F-019.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `9019` | Target nucleus: F-19 |
| AWR | `18.83520` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `304` | Lines of descriptive text |
| NXC | `69` | Data sections in this file |

## Description

  9-F - 19 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL  925
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 22 (a,na) reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 22 (a,na) reaction
    Calculated with the CCONE code /1/.

  MT= 28 (a,np) reaction
    Calculated with the CCONE code /1/.

  MT= 50-77 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-12 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

 MF=1  General Information
   MT=451  Comments and Dictionary

 MF=3  (a,n) Reaction Cross Sections
   MT=4    Neutron Production Cross Section
       The experimental data measured by Norman et al./1/ were
       compaired with the data derived from the thick target neut-
       ron yields measured by Bair and Gomez del Campo /2/, and
       by Jacobs and Liskien /3/. The data by Jacobs and Liskien
       agree well with the data by Norman et al., but the data by
       Bair and Gomez del Campo are a little lower than them. The
       stopping powers given by Ziegler /4/ were used for this
       derivation.
       The data by Norman et al. were analyzed by using the
       EGNASH-2 program /5/ , and good agreement were obtained
       between the both. The evaluated values were obtained by
       calculation with this program in the alpha energy range
       from the threshold energy (2.3629 MeV) to 15 MeV.
       The level schemes of target and residual nuclei were taken
       from Ref./6/ as follows.

                    Target (F-19)           Residual (Na-22)
           Level  Energy  Spin-Parity     Energy  Spin-Parity
            No.   (MeV)                   (MeV)
           G.S.   0.0000   0.5  +         0.0000   3.0  +
             1    0.10989  0.5  -         0.5830   1.0  +
             2    0.19715  2.5  +         0.6570   0.0  +
             3    1.3457   2.5  -         0.8909   4.0  +
             4    1.4585   1.5  -         1.5281   5.0  +
             5    1.5541   1.5  +         1.9369   1.0  +
             6    2.780    4.5  +         1.9519   2.0  +
             7    3.907    1.5  +         1.9840   3.0  +
             8    3.999    3.5  -         2.2115   1.0  -
             9    4.032    4.5  -         2.5715   2.0  -
            10    4.378    3.5  +         2.969    3.0  +
            11    4.549    2.5  +         3.060    2.0  +
            12    4.558    1.5  -         3.519    3.0  -
            13    4.648    6.5  +         3.707    6.0  +
            14    4.683    2.5  -         3.942    1.0  +
            15    5.106    2.5  +         4.071    4.0  +
            16    5.336    0.5  +         4.296    2.0  +
            17    5.43     3.5  -         4.319    1.0  +
            18    5.464    3.5  +         4.360    2.0  +
            19    5.499    1.5  +         4.469    4.0  -
            20    5.540    2.5  +         4.524    7.0  +
            21    5.618    1.5  -         4.583    3.0  -
            22    5.938    0.5  +         4.622    1.0  +
            23    6.499    5.5  +         4.710    5.0  +
            24    6.592    4.5  +         4.772    3.0  +
            25    7.166    5.5  -         5.062    2.0  +
            26    7.935    5.5  +         5.100    4.0  +
            27    8.288    6.5  -         5.166    2.0  +
            28    8.957    5.5  +
            29   10.411    6.5  +

       The continuum levels of Na-22 were assumed above 5.317 MeV.

   MT=22   (a,na) and (a,an) Reaction Cross Sections
       Calculated by using the EGNASH-2 program.

   MT=28   (a,np) and (a,pn) Reaction Cross Sections
       Calculated by using the EGNASH-2 program.

   MT=50   (a,n) Cross Section to the Ground State
       Calculated by using the EGNASH-2 program.

   MT=51-77  (a,n) Cross Sections to the Discrete Excited Levels
       Calculated by using the EGNASH-2 program.

   MT=91   (a,n) Cross Section to the Continuum Levels
       Obtained by subtracting the (a,na), (a,np), and (a,n)
       reaction cross sections to the ground state and discrete
       excited levels from the total (a,n) reaction cross section.

   MT=201  Total neutron production cross sections
       Sum of MT=4, 22, 28, 50-77, 91

 MF=6  Neutron Energy-Angle Distributions
   MT=201  Total Neutron Production Spectra
       Calculated by using the EGNASH-2 program. These neutron
       spectra consist of the following three contribution.
         1. (a,n) reaction in the energy range from the threshold
                  (2.3629 MeV) to 15 MeV.
         2. (a,np) and (a,pn) reactions above 10.5221 MeV.
         3. (a,na) and (a,an) reactions above 12.6300 MeV.

   Thick Target Neutron Yield
       Calculated by using the cross sections of (a,n), (a,np),
       (a,pn), (a,na), and (a,an) reactions evaluated in the
       present work, and the stopping powers by Ziegler /4/.
       The result is shown as follows.

              No.  Energy   Gas Target      Solid Target
                    (MeV) (neutron/alpha) (neutron/alpha)
                1    2.4    3.78767E-11     4.11430E-11
                2    2.5    6.39534E-10     6.93487E-10
                3    2.6    2.30119E-09     2.49033E-09
                4    2.7    5.64805E-09     6.09992E-09
                5    2.8    1.14142E-08     1.23024E-08
                6    2.9    2.02813E-08     2.18159E-08
                7    3.0    3.27805E-08     3.51923E-08
                8    3.1    5.13394E-08     5.50042E-08
                9    3.2    8.18752E-08     8.75220E-08
               10    3.3    1.29875E-07     1.38515E-07
               11    3.4    1.98222E-07     2.10957E-07
               12    3.5    2.89386E-07     3.07364E-07
               13    3.6    4.05565E-07     4.29954E-07
               14    3.7    5.48484E-07     5.80441E-07
               15    3.8    7.20801E-07     7.61506E-07
               16    3.9    9.25178E-07     9.75829E-07
               17    4.0    1.16323E-06     1.22499E-06
               18    4.1    1.43601E-06     1.50996E-06
               19    4.2    1.74370E-06     1.83082E-06
               20    4.3    2.08658E-06     2.18775E-06
               21    4.4    2.46607E-06     2.58214E-06
               22    4.5    2.88393E-06     3.01570E-06
               23    4.6    3.34104E-06     3.48924E-06
               24    4.7    3.83756E-06     4.00285E-06
               25    4.8    4.38768E-06     4.57108E-06
               26    4.9    5.00328E-06     5.20606E-06
               27    5.0    5.68164E-06     5.90485E-06
               28    5.1    6.42541E-06     6.67003E-06
               29    5.2    7.23973E-06     7.50676E-06
               30    5.3    8.12689E-06     8.41726E-06
               31    5.4    9.08542E-06     9.39988E-06
               32    5.5    1.01132E-05     1.04523E-05
               33    5.6    1.12113E-05     1.15756E-05
               34    5.7    1.23808E-05     1.27708E-05
               35    5.8    1.36183E-05     1.40341E-05
               36    5.9    1.49186E-05     1.53603E-05
               37    6.0    1.62793E-05     1.67469E-05
               38    6.1    1.77012E-05     1.81947E-05
               39    6.2    1.91847E-05     1.97038E-05
               40    6.3    2.07282E-05     2.12728E-05
               41    6.4    2.23286E-05     2.28983E-05
               42    6.5    2.39834E-05     2.45779E-05
               43    6.6    2.56905E-05     2.63093E-05
               44    6.7    2.74503E-05     2.80929E-05
               45    6.8    2.92642E-05     2.99302E-05
               46    6.9    3.11312E-05     3.18200E-05
               47    7.0    3.30496E-05     3.37607E-05
               48    7.1    3.50177E-05     3.57505E-05
               49    7.2    3.70350E-05     3.77888E-05
               50    7.3    3.91013E-05     3.98757E-05
               51    7.4    4.12173E-05     4.20115E-05
               52    7.5    4.33826E-05     4.41960E-05
               53    7.6    4.55962E-05     4.64282E-05
               54    7.7    4.78612E-05     4.87110E-05
               55    7.8    5.01798E-05     5.10469E-05
               56    7.9    5.25523E-05     5.34361E-05
               57    8.0    5.49823E-05     5.58821E-05
               58    8.1    5.74729E-05     5.83881E-05
               59    8.2    6.00257E-05     6.09557E-05
               60    8.3    6.26386E-05     6.35828E-05
               61    8.4    6.53057E-05     6.62634E-05
               62    8.5    6.80202E-05     6.89907E-05
               63    8.6    7.07804E-05     7.17630E-05
               64    8.7    7.35876E-05     7.45815E-05
               65    8.8    7.64371E-05     7.74417E-05
               66    8.9    7.93414E-05     8.03560E-05
               67    9.0    8.23447E-05     8.33687E-05
               68    9.1    8.54604E-05     8.64933E-05
               69    9.2    8.86322E-05     8.96733E-05
               70    9.3    9.18655E-05     9.29142E-05
               71    9.4    9.51651E-05     9.62206E-05
               72    9.5    9.84763E-05     9.95378E-05
               73    9.6    1.01842E-04     1.02909E-04
               74    9.7    1.05258E-04     1.06330E-04
               75    9.8    1.08723E-04     1.09799E-04
               76    9.9    1.12248E-04     1.13326E-04
               77   10.0    1.15818E-04     1.16899E-04
               78   10.1    1.19440E-04     1.20523E-04
               79   10.2    1.23069E-04     1.24153E-04
               80   10.3    1.26740E-04     1.27825E-04
               81   10.4    1.30480E-04     1.31564E-04
               82   10.5    1.34273E-04     1.35357E-04
               83   10.6    1.38127E-04     1.39210E-04
               84   10.7    1.42014E-04     1.43094E-04
               85   10.8    1.45939E-04     1.47017E-04
               86   10.9    1.49926E-04     1.51000E-04
               87   11.0    1.53952E-04     1.55023E-04
               88   11.1    1.58042E-04     1.59107E-04
               89   11.2    1.62191E-04     1.63252E-04
               90   11.3    1.66390E-04     1.67445E-04
               91   11.4    1.70650E-04     1.71698E-04
               92   11.5    1.74937E-04     1.75978E-04
               93   11.6    1.79296E-04     1.80329E-04
               94   11.7    1.83714E-04     1.84739E-04
               95   11.8    1.88138E-04     1.89154E-04
               96   11.9    1.92627E-04     1.93633E-04
               97   12.0    1.97165E-04     1.98162E-04
               98   12.1    2.01709E-04     2.02696E-04
               99   12.2    2.06314E-04     2.07289E-04
              100   12.3    2.10967E-04     2.11931E-04
              101   12.4    2.15674E-04     2.16626E-04
              102   12.5    2.20439E-04     2.21377E-04
              103   12.6    2.25198E-04     2.26124E-04
              104   12.7    2.29943E-04     2.30855E-04
              105   12.8    2.34673E-04     2.35571E-04
              106   12.9    2.39385E-04     2.40269E-04
              107   13.0    2.44108E-04     2.44978E-04
              108   13.1    2.48887E-04     2.49742E-04
              109   13.2    2.53702E-04     2.54541E-04
              110   13.3    2.58544E-04     2.59366E-04
              111   13.4    2.63423E-04     2.64229E-04
              112   13.5    2.68334E-04     2.69123E-04
              113   13.6    2.73278E-04     2.74050E-04
              114   13.7    2.78256E-04     2.79010E-04
              115   13.8    2.83253E-04     2.83989E-04
              116   13.9    2.88278E-04     2.88996E-04
              117   14.0    2.93324E-04     2.94023E-04
              118   14.1    2.98388E-04     2.99068E-04
              119   14.2    3.03500E-04     3.04161E-04
              120   14.3    3.08642E-04     3.09283E-04
              121   14.4    3.13807E-04     3.14428E-04
              122   14.5    3.18988E-04     3.19589E-04
              123   14.6    3.24178E-04     3.24757E-04
              124   14.7    3.29394E-04     3.29953E-04
              125   14.8    3.34645E-04     3.35183E-04
              126   14.9    3.39928E-04     3.40443E-04
              127   15.0    3.45211E-04     3.45705E-04

 References
 1) Norman,E.B., Chupp,T.E., Lesko,K.T., Grant,P.J., and
    Woodruff,G.L. : Phys. Rev. C 30, 1339 (1984)
 2) Bair,J.K. and Gomez del Campo,J : Nucl. Sci. Eng. 71,18 (1979)
 3) Jacobs,J.G.H. and Liskien,H.: Ann. Nucl. Energy 10, 541 (1983)
 4) Ziegler,J.F. :"Helium Stopping Powers and Ranges in All
                   Elemental Matter" Pergamon Press, Oxford (1977)
 5) Yamamuro,N.: "A Nuclear Cross Section Calculation System with
                  Simplified Input-Format" Version II (SINCROS-II)
                  February 1990,  JAERI-M 90-006 (1990)
 6) Lederer C.M. and Shirley V.S.: Table of Isotopes (7th Edition)


## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 377 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 26 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 22 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 26 | Original |
| 3 | 22 | Cross sections: (α,nα) reaction | 10 | Supplement |
| 3 | 28 | Cross sections: (α,pn) reaction | 19 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 12 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 12 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 12 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 12 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 11 | Supplement |
| 3 | 55 | Cross sections: MT=55 | 11 | Supplement |
| 3 | 56 | Cross sections: MT=56 | 11 | Supplement |
| 3 | 57 | Cross sections: MT=57 | 11 | Supplement |
| 3 | 58 | Cross sections: MT=58 | 10 | Supplement |
| 3 | 59 | Cross sections: MT=59 | 10 | Supplement |
| 3 | 60 | Cross sections: MT=60 | 10 | Supplement |
| 3 | 61 | Cross sections: MT=61 | 10 | Supplement |
| 3 | 62 | Cross sections: MT=62 | 9 | Supplement |
| 3 | 63 | Cross sections: MT=63 | 9 | Supplement |
| 3 | 64 | Cross sections: MT=64 | 9 | Supplement |
| 3 | 65 | Cross sections: MT=65 | 9 | Supplement |
| 3 | 66 | Cross sections: MT=66 | 9 | Supplement |
| 3 | 67 | Cross sections: MT=67 | 9 | Supplement |
| 3 | 68 | Cross sections: MT=68 | 9 | Supplement |
| 3 | 69 | Cross sections: MT=69 | 9 | Supplement |
| 3 | 70 | Cross sections: MT=70 | 9 | Supplement |
| 3 | 71 | Cross sections: MT=71 | 9 | Supplement |
| 3 | 72 | Cross sections: MT=72 | 9 | Supplement |
| 3 | 73 | Cross sections: MT=73 | 8 | Supplement |
| 3 | 74 | Cross sections: MT=74 | 8 | Supplement |
| 3 | 75 | Cross sections: MT=75 | 8 | Supplement |
| 3 | 76 | Cross sections: MT=76 | 8 | Supplement |
| 3 | 77 | Cross sections: MT=77 | 8 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 8 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 34 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 2,114 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 84,091 | Original |
| 6 | 22 | Energy-angle distributions: (α,nα) reaction | 107 | Supplement |
| 6 | 28 | Energy-angle distributions: (α,pn) reaction | 167 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 185 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 183 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 191 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 167 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 146 | Supplement |
| 6 | 55 | Energy-angle distributions: MT=55 | 161 | Supplement |
| 6 | 56 | Energy-angle distributions: MT=56 | 157 | Supplement |
| 6 | 57 | Energy-angle distributions: MT=57 | 149 | Supplement |
| 6 | 58 | Energy-angle distributions: MT=58 | 147 | Supplement |
| 6 | 59 | Energy-angle distributions: MT=59 | 145 | Supplement |
| 6 | 60 | Energy-angle distributions: MT=60 | 114 | Supplement |
| 6 | 61 | Energy-angle distributions: MT=61 | 117 | Supplement |
| 6 | 62 | Energy-angle distributions: MT=62 | 102 | Supplement |
| 6 | 63 | Energy-angle distributions: MT=63 | 92 | Supplement |
| 6 | 64 | Energy-angle distributions: MT=64 | 92 | Supplement |
| 6 | 65 | Energy-angle distributions: MT=65 | 91 | Supplement |
| 6 | 66 | Energy-angle distributions: MT=66 | 82 | Supplement |
| 6 | 67 | Energy-angle distributions: MT=67 | 78 | Supplement |
| 6 | 68 | Energy-angle distributions: MT=68 | 76 | Supplement |
| 6 | 69 | Energy-angle distributions: MT=69 | 70 | Supplement |
| 6 | 70 | Energy-angle distributions: MT=70 | 67 | Supplement |
| 6 | 71 | Energy-angle distributions: MT=71 | 63 | Supplement |
| 6 | 72 | Energy-angle distributions: MT=72 | 61 | Supplement |
| 6 | 73 | Energy-angle distributions: MT=73 | 58 | Supplement |
| 6 | 74 | Energy-angle distributions: MT=74 | 57 | Supplement |
| 6 | 75 | Energy-angle distributions: MT=75 | 49 | Supplement |
| 6 | 76 | Energy-angle distributions: MT=76 | 47 | Supplement |
| 6 | 77 | Energy-angle distributions: MT=77 | 43 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 385 | Supplement |

---

# Na-23  (Z=11, A=23)
**File:** `a_011-Na-023.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `11023` | Target nucleus: Na-23 |
| AWR | `22.79228` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `276` | Lines of descriptive text |
| NXC | `69` | Data sections in this file |

## Description

 11-Na- 23 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL 1125
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT=4, 50-91 (a,n') reaction
    Taken from JENDL/AN-2005 /2/.

  MT= 28 (a,np) reaction
    Taken from JENDL/AN-2005 /2/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Reactions other than neutron emission channels
    Calculated with the CCONE code /1/.

  MT= 28 (a,np) reaction
    Calculated with the CCONE code /1/.

  MT= 50-78 (a,n') reaction
    Calculated with the CCONE code /1/.

  MT= 91 (a,n') reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
02-12 Compiled by K.Shibata(JAERI).
05-05 Taken from JENDL/AN-2003 without modifications.

 MF=1  General Information
   MT=451  Comments and Dictionary

 MF=3  (a,n) Reaction Cross Sections
   MT=4    Neutron Production Cross Section
       The experimental data measured by Norman et al./1/ and by
       Skelton et al./2/ were analyzed by using the EGNASH-2
       program /3/, and were reproduced well by this analysis.
       The evaluated values were obtained by calculation with this
       program in the alpha energy range from the threshold energy
       (3.48187 MeV) to 15 MeV.
       The level schemes of target and residual nuclei were taken
       from Ref./4/ as follows.

                    Target (Na-23)          Residual (Al-26)
           Level  Energy  Spin-Parity     Energy  Spin-Parity
            No.   (MeV)                   (MeV)
           G.S.   0.0000   1.5  +         0.0000   5.0  +
             1    0.4399   2.5  +         0.2282   0.0  +
             2    2.0764   3.5  +         0.4169   3.0  +
             3    2.3909   0.5  +         1.0578   1.0  +
             4    2.6398   0.5  -         1.759    2.0  +
             5    2.7037   4.5  +         1.851    1.0  +
             6    2.9824   1.5  +         2.0687   4.0  +
             7    3.6783   1.5  -         2.0695   2.0  +
             8    3.848    2.5  -         2.072    1.0  +
             9    3.9147   2.5  +         2.3652   3.0  +
            10    4.432    0.5  +         2.5453   3.0  +
            11    4.7756   3.5  +         2.6608   2.0  +
            12    5.380    2.5  +         2.739    1.0  +
            13    5.536    5.5  +         2.913    2.0  +
            14    5.741    1.5  +         3.074    3.0  +
            15    5.766    2.5  +         3.159    2.0  +
            16    5.931    3.5  +         3.4035   5.0  +
            17    5.967    0.5  -         3.5075   6.0  +
            18    6.043    1.5  -         3.596    2.0  +
            19    6.117    5.5  +         3.672    3.0  +
            20                            3.681    4.0  +
            21                            3.723    1.0  +
            22                            3.750    2.0  +
            23                            3.753    0.0  +
            24                            3.918    7.0  +
            25                            3.962    3.0  +
            26                            3.979    0.0  +
            27                            4.192    2.0  +
            28                            4.205    3.0  +

       The continuum levels of Al-26 were assumed above 4.3 MeV.

   MT=28   (a,np) and (a,pn) Reaction Cross Sections
       Calculated by using the EGNASH-2 program.

   MT=50   (a,n) Cross Section to the Ground State
       Calculated by using the EGNASH-2 program.

   MT=51-78  (a,n) Cross Sections to the Discrete Excited Levels
       Calculated by using the EGNASH-2 program.

   MT=91   (a,n) Cross Section to the Continuum Levels
       Obtained by subtracting the (a,np) reaction cross section
       and (a,n) reaction cross sections to the ground state and
       discrete excited levels from the total (a,n) reaction cross
       section.

   MT=201  Total Neutron Production Cross Sections
       Sum of MT=4, 28, 50-78, 91

 MF=6  Neutron Energy-Angle Distributions
   MT=201  Total Neutron Production Spectra
       Calculated by using the EGNASH-2 program. These neutron
       spectra consist of the following two contribution.
         1. (a,n) reaction in the energy range from the threshold
                  (3.48187 MeV) to 15 MeV.
         2. (a,np) and (a,pn) reactions above 10.8865 MeV.

   Thick Target Neutron Yield
       Calculated by using the cross sections of (a,n), (a,np),
       and (a,pn) reactions evaluated in the present work, and the
       stopping powers given by Ziegler /5/.
       The result is shown as follows.

              No.  Energy   Gas Target      Solid Target
                    (MeV) (neutron/alpha) (neutron/alpha)
                1    3.5    9.06994E-11     8.93518E-11
                2    3.6    2.25635E-09     2.22125E-09
                3    3.7    6.68315E-09     6.57400E-09
                4    3.8    1.38639E-08     1.36274E-08
                5    3.9    2.50570E-08     2.46123E-08
                6    4.0    4.41869E-08     4.33718E-08
                7    4.1    7.65582E-08     7.50957E-08
                8    4.2    1.24501E-07     1.22054E-07
                9    4.3    1.89000E-07     1.85199E-07
               10    4.4    2.71287E-07     2.65729E-07
               11    4.5    3.72352E-07     3.64608E-07
               12    4.6    4.92969E-07     4.82588E-07
               13    4.7    6.33479E-07     6.20008E-07
               14    4.8    7.98664E-07     7.81545E-07
               15    4.9    9.93112E-07     9.71691E-07
               16    5.0    1.21687E-06     1.19051E-06
               17    5.1    1.46962E-06     1.43769E-06
               18    5.2    1.75029E-06     1.71220E-06
               19    5.3    2.05788E-06     2.01309E-06
               20    5.4    2.39090E-06     2.33891E-06
               21    5.5    2.74869E-06     2.68905E-06
               22    5.6    3.13377E-06     3.06600E-06
               23    5.7    3.55287E-06     3.47636E-06
               24    5.8    4.00943E-06     3.92352E-06
               25    5.9    4.50219E-06     4.40631E-06
               26    6.0    5.04160E-06     4.93499E-06
               27    6.1    5.63827E-06     5.52000E-06
               28    6.2    6.28703E-06     6.15633E-06
               29    6.3    6.98579E-06     6.84198E-06
               30    6.4    7.73393E-06     7.57639E-06
               31    6.5    8.53141E-06     8.35958E-06
               32    6.6    9.37775E-06     9.19112E-06
               33    6.7    1.02735E-05     1.00716E-05
               34    6.8    1.12233E-05     1.10057E-05
               35    6.9    1.22187E-05     1.19850E-05
               36    7.0    1.32562E-05     1.30063E-05
               37    7.1    1.43334E-05     1.40672E-05
               38    7.2    1.54467E-05     1.51642E-05
               39    7.3    1.65979E-05     1.62991E-05
               40    7.4    1.77867E-05     1.74716E-05
               41    7.5    1.90147E-05     1.86835E-05
               42    7.6    2.02778E-05     1.99306E-05
               43    7.7    2.15810E-05     2.12180E-05
               44    7.8    2.29262E-05     2.25476E-05
               45    7.9    2.43183E-05     2.39242E-05
               46    8.0    2.57667E-05     2.53573E-05
               47    8.1    2.72603E-05     2.68359E-05
               48    8.2    2.87981E-05     2.83590E-05
               49    8.3    3.03763E-05     2.99231E-05
               50    8.4    3.19918E-05     3.15249E-05
               51    8.5    3.36777E-05     3.31974E-05
               52    8.6    3.54277E-05     3.49345E-05
               53    8.7    3.72306E-05     3.67249E-05
               54    8.8    3.90890E-05     3.85715E-05
               55    8.9    4.10022E-05     4.04735E-05
               56    9.0    4.29701E-05     4.24310E-05
               57    9.1    4.50040E-05     4.44552E-05
               58    9.2    4.70913E-05     4.65336E-05
               59    9.3    4.92409E-05     4.86753E-05
               60    9.4    5.14511E-05     5.08783E-05
               61    9.5    5.37205E-05     5.31417E-05
               62    9.6    5.60622E-05     5.54783E-05
               63    9.7    5.84405E-05     5.78527E-05
               64    9.8    6.08809E-05     6.02904E-05
               65    9.9    6.33927E-05     6.28006E-05
               66   10.0    6.59761E-05     6.53839E-05
               67   10.1    6.86070E-05     6.80158E-05
               68   10.2    7.13008E-05     7.07122E-05
               69   10.3    7.40656E-05     7.34809E-05
               70   10.4    7.68635E-05     7.62842E-05
               71   10.5    7.97190E-05     7.91467E-05
               72   10.6    8.26418E-05     8.20781E-05
               73   10.7    8.56202E-05     8.50668E-05
               74   10.8    8.86362E-05     8.80946E-05
               75   10.9    9.16865E-05     9.11585E-05
               76   11.0    9.47939E-05     9.42813E-05
               77   11.1    9.79516E-05     9.74560E-05
               78   11.2    1.01128E-04     1.00651E-04
               79   11.3    1.04338E-04     1.03882E-04
               80   11.4    1.07594E-04     1.07160E-04
               81   11.5    1.10881E-04     1.10471E-04
               82   11.6    1.14213E-04     1.13829E-04
               83   11.7    1.17560E-04     1.17204E-04
               84   11.8    1.20916E-04     1.20590E-04
               85   11.9    1.24319E-04     1.24024E-04
               86   12.0    1.27736E-04     1.27474E-04
               87   12.1    1.31158E-04     1.30931E-04
               88   12.2    1.34617E-04     1.34426E-04
               89   12.3    1.38091E-04     1.37940E-04
               90   12.4    1.41591E-04     1.41479E-04
               91   12.5    1.45150E-04     1.45081E-04
               92   12.6    1.48735E-04     1.48711E-04
               93   12.7    1.52366E-04     1.52389E-04
               94   12.8    1.56060E-04     1.56132E-04
               95   12.9    1.59773E-04     1.59896E-04
               96   13.0    1.63518E-04     1.63694E-04
               97   13.1    1.67310E-04     1.67542E-04
               98   13.2    1.71149E-04     1.71438E-04
               99   13.3    1.75029E-04     1.75380E-04
              100   13.4    1.78956E-04     1.79369E-04
              101   13.5    1.82922E-04     1.83400E-04
              102   13.6    1.86927E-04     1.87472E-04
              103   13.7    1.91069E-04     1.91685E-04
              104   13.8    1.95344E-04     1.96036E-04
              105   13.9    1.99642E-04     2.00412E-04
              106   14.0    2.03973E-04     2.04822E-04
              107   14.1    2.08341E-04     2.09274E-04
              108   14.2    2.12739E-04     2.13756E-04
              109   14.3    2.17178E-04     2.18283E-04
              110   14.4    2.21639E-04     2.22834E-04
              111   14.5    2.26107E-04     2.27393E-04
              112   14.6    2.30597E-04     2.31977E-04
              113   14.7    2.35114E-04     2.36590E-04
              114   14.8    2.39651E-04     2.41226E-04
              115   14.9    2.44204E-04     2.45880E-04
              116   15.0    2.48790E-04     2.50569E-04

 References
 1) Norman,E.B., Chupp,T.E., Lesko,K.T., and Schwalbach,P.
                                 : Nucl. Phys. A 390 561 (1982)
 2) Skelton,R.T., Kavanagh,R.W., and Sargood,D.G.
                                 : Phys. Rev. C 35, 45 (1987)
 3) Yamamuro,N.: "A Nuclear Cross Section Calculation System with
                  Simplified Input-Format" Version II (SINCROS-II)
                  February 1990,  JAERI-M 90-006 (1990)
 4) Lederer C.M. and Shirley V.S.: Table of Isotopes (7th Edition)
 5) Ziegler,J.F. :"Helium Stopping Powers and Ranges in All
                   Elemental Matter" Pergamon Press, Oxford (1977)


## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 349 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 27 | Original |
| 3 | 4 | Cross sections: (α,n) — neutron emission (other than to discrete states) | 21 | Supplement |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 27 | Original |
| 3 | 28 | Cross sections: (α,pn) reaction | 18 | Supplement |
| 3 | 50 | Cross sections: (α,n₀) — to ground state | 12 | Supplement |
| 3 | 51 | Cross sections: (α,n₁) — to 1st excited state | 11 | Supplement |
| 3 | 52 | Cross sections: (α,n₂) — to 2nd excited state | 11 | Supplement |
| 3 | 53 | Cross sections: (α,n₃) — to 3rd excited state | 11 | Supplement |
| 3 | 54 | Cross sections: (α,n₄) — to 4th excited state | 10 | Supplement |
| 3 | 55 | Cross sections: MT=55 | 10 | Supplement |
| 3 | 56 | Cross sections: MT=56 | 10 | Supplement |
| 3 | 57 | Cross sections: MT=57 | 10 | Supplement |
| 3 | 58 | Cross sections: MT=58 | 10 | Supplement |
| 3 | 59 | Cross sections: MT=59 | 10 | Supplement |
| 3 | 60 | Cross sections: MT=60 | 10 | Supplement |
| 3 | 61 | Cross sections: MT=61 | 9 | Supplement |
| 3 | 62 | Cross sections: MT=62 | 9 | Supplement |
| 3 | 63 | Cross sections: MT=63 | 9 | Supplement |
| 3 | 64 | Cross sections: MT=64 | 9 | Supplement |
| 3 | 65 | Cross sections: MT=65 | 9 | Supplement |
| 3 | 66 | Cross sections: MT=66 | 9 | Supplement |
| 3 | 67 | Cross sections: MT=67 | 9 | Supplement |
| 3 | 68 | Cross sections: MT=68 | 9 | Supplement |
| 3 | 69 | Cross sections: MT=69 | 9 | Supplement |
| 3 | 70 | Cross sections: MT=70 | 9 | Supplement |
| 3 | 71 | Cross sections: MT=71 | 9 | Supplement |
| 3 | 72 | Cross sections: MT=72 | 9 | Supplement |
| 3 | 73 | Cross sections: MT=73 | 9 | Supplement |
| 3 | 74 | Cross sections: MT=74 | 8 | Supplement |
| 3 | 75 | Cross sections: MT=75 | 8 | Supplement |
| 3 | 76 | Cross sections: MT=76 | 8 | Supplement |
| 3 | 77 | Cross sections: MT=77 | 8 | Supplement |
| 3 | 78 | Cross sections: MT=78 | 8 | Supplement |
| 3 | 91 | Cross sections: (α,n) continuum | 8 | Supplement |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 33 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 2,176 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 85,296 | Original |
| 6 | 28 | Energy-angle distributions: (α,pn) reaction | 142 | Supplement |
| 6 | 50 | Energy-angle distributions: (α,n₀) — to ground state | 173 | Supplement |
| 6 | 51 | Energy-angle distributions: (α,n₁) — to 1st excited state | 185 | Supplement |
| 6 | 52 | Energy-angle distributions: (α,n₂) — to 2nd excited state | 170 | Supplement |
| 6 | 53 | Energy-angle distributions: (α,n₃) — to 3rd excited state | 165 | Supplement |
| 6 | 54 | Energy-angle distributions: (α,n₄) — to 4th excited state | 140 | Supplement |
| 6 | 55 | Energy-angle distributions: MT=55 | 146 | Supplement |
| 6 | 56 | Energy-angle distributions: MT=56 | 136 | Supplement |
| 6 | 57 | Energy-angle distributions: MT=57 | 132 | Supplement |
| 6 | 58 | Energy-angle distributions: MT=58 | 141 | Supplement |
| 6 | 59 | Energy-angle distributions: MT=59 | 119 | Supplement |
| 6 | 60 | Energy-angle distributions: MT=60 | 117 | Supplement |
| 6 | 61 | Energy-angle distributions: MT=61 | 109 | Supplement |
| 6 | 62 | Energy-angle distributions: MT=62 | 127 | Supplement |
| 6 | 63 | Energy-angle distributions: MT=63 | 102 | Supplement |
| 6 | 64 | Energy-angle distributions: MT=64 | 96 | Supplement |
| 6 | 65 | Energy-angle distributions: MT=65 | 92 | Supplement |
| 6 | 66 | Energy-angle distributions: MT=66 | 84 | Supplement |
| 6 | 67 | Energy-angle distributions: MT=67 | 84 | Supplement |
| 6 | 68 | Energy-angle distributions: MT=68 | 84 | Supplement |
| 6 | 69 | Energy-angle distributions: MT=69 | 81 | Supplement |
| 6 | 70 | Energy-angle distributions: MT=70 | 77 | Supplement |
| 6 | 71 | Energy-angle distributions: MT=71 | 81 | Supplement |
| 6 | 72 | Energy-angle distributions: MT=72 | 77 | Supplement |
| 6 | 73 | Energy-angle distributions: MT=73 | 83 | Supplement |
| 6 | 74 | Energy-angle distributions: MT=74 | 72 | Supplement |
| 6 | 75 | Energy-angle distributions: MT=75 | 69 | Supplement |
| 6 | 76 | Energy-angle distributions: MT=76 | 68 | Supplement |
| 6 | 77 | Energy-angle distributions: MT=77 | 54 | Supplement |
| 6 | 78 | Energy-angle distributions: MT=78 | 58 | Supplement |
| 6 | 91 | Energy-angle distributions: (α,n) continuum | 391 | Supplement |

---

# Al-27  (Z=13, A=27)
**File:** `a_013-Al-027.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `13027` | Target nucleus: Al-27 |
| AWR | `26.74975` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `104` | Lines of descriptive text |
| NXC | `7` | Data sections in this file |

## Description

 13-Al- 27 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL 1325
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
05-05 Evaluated by T.Murata(AITEL), compiled by K.Shibata(JAERI).

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       -2.6363               3.0274
   (a,2n)     -11.3965              13.0871
   (a,pn)      -8.2373               9.4593

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
      Incident alpha particle energy Ea below 5.5MeV,experimental
    cross sections were measured by Holmqvist/1/ and Flynn/2/ and
    shows resonance structures. Excitation energy region of the
    compound nucleus P-31 is above 10MeV and level structures are
    so complicated that detailed resonance analysis is difficult.
    Evaluated cross section was obtained by tracing the experimen-
    tal cross sections.
      In the energy region Ea>=5.5MeV, Stelson/3/ measured the
    cross sections by neutron counting. Sahakundu/4/ measured P-30
    production cross sections above Ea>10MeV, which do not corres-
    pond to neutron production cross section in the energy region
    Ea>=9.46MeV, where produced P-30 decay mainly by proton emiss-
    ion. Evaluated cross sections were obtained by normalizing
    the calculated cross sections with EGNASH2 code/5/ to the
    cross sections in the energy region Ea<=5.5MeV.
      The evaluated cross sections were compared with the experi-
    mental thick target neutron yields measured by Bair/6/ and by
    West/7/ and are slightly modified to reproduce the experimen-
    tal data.

MF=6 Product Energy-Angle Distributions
 MT=201 Neutrons
      Energy-angle distributions of produced neutrons were calcu-
    lated with EGNASH-2 code. They are given in Kalbach's systema-
    tics/8/(LAW=1,LANG=2) including some discrete level transi-
    tions( ground state transition only for the present case).



References
/1/ B.Holmqvist,E.Ramstrom: Physica Scripta 33,107(1986)
/2/ D.S.Flynn et al.: Phys.Rev. C18,1566(1978)
/3/ R.H.Stelson,F.K.Mcgowan: Phys.Rev. B133,911(1964)
/4/ S.M.Sahakundu, S.M.Qaim, G.Stocklin:
    Applied Radiation and Isotopes 30,3(1979)
/5/ N.Yamamuro: JAERI-M 90-006 (1990)
/6/ J.K.Bair,J.Gomez del Campo: Nucl.Sci.Eng.,71,18(1979)
/7/ D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/8/ C.Kalbach: Phys.Rev.C37,2350(1988)



## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 115 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 21 | Original |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 21 | Original |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 126 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,680 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 65,571 | Original |
| 6 | 201 | Energy-angle distributions: (α,xn) — total neutron production | 14,134 | Supplement |

---

# Si-28  (Z=14, A=28)
**File:** `a_014-Si-028.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `14028` | Target nucleus: Si-28 |
| AWR | `27.73659` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `99` | Lines of descriptive text |
| NXC | `7` | Data sections in this file |

## Description

 14-Si- 28 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL 1425
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
05-05 Evaluated by T.Murata(AITEL), compiled by K.Shibata(JAERI).


MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       -8.0943              9.2523

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
      Experimental cross sections were measured by Cheng and King
    /1/ in the incident alpha particle energy range Ea=8-11MeV.
     Evaluation of the cross section was made by tracing the expe-
    rimental cross sections. Extrapolation of the cross section to
     higher energy was made by calculation with EGNASH2 code/2/.
      The evaluated cross sections were compared with the experi-
    mental thick target neutron yields of natural Si measured by
    Bair/3/ and by West/4/ and are slightly modified to reproduce
    the experimental data.

MF=6 Product Energy-Angle Distributions
 MT=201 Neutrons
      Energy-angle distributions of produced neutron were calcu-
    lated with EGNASH-2 code. They are given in Kalbach's systema-
    tics/5/(LAW=1,LANG=2) including some discrete level transi-
    tions. The following level scheme of S-31 was set in  EGNASH2
    library.

      S-31:residual nucleus of the Si28(a,n)reaction
           Ex(MeV)          spin-parity
           0.0000              1/2+
           1.2489              3/2+
           2.2356              5/2+
           3.0790              1/2+
           3.2855              5/2+
           3.3511              3/2+
           3.4370              3/2+
      Levels above Ex=3.079MeV were assumed to continuum


References
/1/ Cheng,C.W.,King,J.D.: Can.J.Phys.58,697,(1980)
/2/ N.Yamamuro: JAERI-M 90-006 (1990)
/3/ J.K.Bair, J.Gomez del Campo: Nucl.Sci.Eng.,71,18(1979)
/4/ D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/5/ C.Kalbach: Phys.Rev.C37,2350(1988)


## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 110 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 24 | Original |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 24 | Original |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 52 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,897 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 63,178 | Original |
| 6 | 201 | Energy-angle distributions: (α,xn) — total neutron production | 5,729 | Supplement |

---

# Si-29  (Z=14, A=29)
**File:** `a_014-Si-029.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `14029` | Target nucleus: Si-29 |
| AWR | `28.72757` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `111` | Lines of descriptive text |
| NXC | `7` | Data sections in this file |

## Description

 14-Si- 29 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL 1428
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
05-05 Evaluated by T.Murata(AITEL), compiled by K.Shibata(JAERI).

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       -1.5263              1.7371
   (a,np)      -10.391              11.826

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
      Experimental cross sections were measured by Flynn et al./1/
    and by Gibbons and Macklin/2/in the incident alpha particle
    energy range Ea=2.7-6.7MeV. The experimental data shows so
    complex resonance structures that resonance analysis cannot
    be made easily. Evaluated cross section was obtained by trac-
    ing the experimental cross sections. Above this energy range,
    evaluated cross sections were obtained by normalizing the cal-
    culated cross sections with EGNASH2 code/3/ to the cross sect-
    ions in the energy region Ea<=6.7MeV.
      The evaluated cross sections were compared with the experi-
    mental thick target neutron yields of natural Si measured by
    Bair/4/ and by West/5/ and are slightly modified to reproduce
    the experimental data.

MF=6 Product Energy-Angle Distributions
 MT=201 Neutrons
      Energy-angle distributions of produced neutrons were calcu-
    lated with EGNASH-2 code. They are given in Kalbach's systema-
    tics/6/(LAW=1,LANG=2) including some discrete level transi-
    tions. The following level scheme of S-32 was set in  EGNASH2
    library.

      S-32:residual nucleus of the Si29(a,n)reaction
           Ex(MeV)          spin-parity
           0.0000               0+
           2.2303               2+
           3.7783               0+
           4.2815               2+
           4.4589               4+
           4.6954               1+
           5.0062               3-
           5.4130               3+
           5.5489               2+
           5.7979               1-
           6.2243               2-
           6.4110               4+
           6.5810               0
           6.6211               4-
      Levels above Ex=6.224 MeV were assumed to continuum


References
/1/ D.S.Flynn,K.K.Sekharan,B.A.Hiller,H.Laumer,J.L.Weil,F.Gabbard:
    Phys.Rev.C18,1566(1978)
/2/ J.H.Gibbons,R.L.Macklin: Phys.Rev.114,579(1959)
/3/ N.Yamamuro: JAERI-M 90-006 (1990)
/4/ J.K.Bair, J.Gomez del Campo: Nucl.Sci.Eng.,71,18(1979)
/5/ D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/6/ C.Kalbach: Phys.Rev.C37,2350(1988)

## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 122 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 25 | Original |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 25 | Original |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 690 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 2,021 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 58,940 | Original |
| 6 | 201 | Energy-angle distributions: (α,xn) — total neutron production | 24,114 | Supplement |

---

# Si-30  (Z=14, A=30)
**File:** `a_014-Si-030.dat`  |  **Library:** JENDL-5  |  **Sublibrary:** Incident α particles  |  **Max energy:** 15 MeV

| Parameter | Value | Meaning |
|---|---|---|
| ZA | `14030` | Target nucleus: Si-30 |
| AWR | `29.71628` | Target mass / neutron mass |
| AWI | `3.96822` | α mass / neutron mass |
| LRP | `-1` | No resonance parameters (charged-particle file) |
| LFI | `0` | Not fissionable |
| NLIB | `6` | JENDL |
| NMOD | `1` | Revision 1 |
| STA | `0` | Stable |
| LIS | `0` | Target: ground state |
| LISO | `0` | Not an isomer |
| NFOR | `6` | ENDF-6 |
| EMAX | `15.0 MeV` | Maximum incident α energy |
| TEMP | `0 K` | Evaluation temperature |
| LREL | `0` | Library release 0 |
| LDRV | `0` | Original evaluation |
| NWD | `112` | Lines of descriptive text |
| NXC | `7` | Data sections in this file |

## Description

 14-Si- 30 JAEA       EVAL-Dec21 S.Nakayama
                      DIST-DEC21                       20211227
----JENDL-5           MATERIAL 1431
-----INCIDENT ALPHA DATA
------ENDF-6 FORMAT

History
2021-12 Evaluated and compiled by S.Nakayama

      *                                                    *
      *                  ---  JENDL-5  ---                 *
      *                                                    *
      *       Alpha-particle sublibrary up to 15 MeV       *
      *                                                    *

MF= 1 General information
  MT=451 Descriptive data and directory

MF= 3 Cross sections
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Taken from JENDL/AN-2005 /2/.

MF= 6 Energy-angle distributions of emitted particles
  MT=  2 Elastic scattering
         (nuclear+interference components)
    Calculated with the CCONE code /1/.

  MT=  5 Total reaction
    Calculated with the CCONE code /1/.

  MT=201 (a,xn) reaction
    Calculated with the CCONE code /1/.

References
 1) O.Iwamoto, J. Nucl. Sci. Technol., 44, 687 (2007)
 2) T.Murata et al., JAEA-Research 2006-052 (2006)

------------------( Comments from JENDL/AN-2005 )-----------------

History
05-05 Evaluated by T.Murata(AITEL), compiled by K.Shibata(JAERI).

MF=1   General Information
 MT=451 Descriptive Data
   The neutron emission reaction channels for incident alpha
   particle energy below 15 MeV are given in the following table.

   Reaction    Q-value (MeV)     Threshold Energy (MeV)
   (a,n)       -3.4942              3.9608
   (a,2n)      -12.136              13.757
   (a,pn)      -13.064              14.809

MF=3   Cross Sections
 MT=201 Neutron Production Cross Section
      Experimental cross sections were measured by Flynn et al./1/
    in the incident alpha particle energy range Ea=4-6.3MeV. The
    experimental data shows so complex resonance structures that
    resonance analysis can not be made easily. Evaluated cross
    section was obtained by tracing the experimentalcross sections
    Above this energy range,evaluated cross sections were obtained
    by normalizing the calculated cross sections with EGNASH2 code
    /2/ to the cross sections in the energy region Ea<=6.3MeV.
    mental thick target neutron yields of natural Si measured by
    Bair/3/ and by West/4/ and are slightly modified to reproduce
    the experimental data.

MF=6 Product Energy-Angle Distributions
 MT=201 Neutrons
      Energy-angle distributions of produced neutron were calcu-
    lated with EGNASH-2 code. They are given in Kalbach's systema-
    tics/5/(LAW=1,LANG=2) including some discrete level transi-
    tions. The following level scheme of S-33 was set in  EGNASH2
    library.

      S-33:residual nucleus of the Si30(a,n)reaction
           Ex(MeV)          spin-parity
            .0000               3/2+
            .8409               1/2+
           1.9663               5/2+
           2.3125               3/2+
           2.8664               5/2+
           2.9337               7/2-
           2.9686               7/2+
           3.2199               3/2-
           3.8316               5/2+
           3.9346               3/2
           4.0476               9/2+
           4.0530               1/2+
           4.0940               7/2+
           4.1437               3/2
           4.2104               3/2-
           4.3749               1/2+
           4.4245               1/2+
        Levels above Ex=3.079MeV were assumed to continuum

References
/1/ D.S.Flynn,K.K.Sekharan,B.A.Hiller,H.Laumer,J.L.Weil,F.Gabbard:
    Phys.Rev.C18,1566(1978)
/2/ N.Yamamuro: JAERI-M 90-006 (1990)
/3/ J.K.Bair, J.Gomez del Campo: Nucl.Sci.Eng.,71,18(1979)
/4/ D.West,A.C.Sherwood:Ann.Nucl.Energy,9,551(1982)
/5/ C.Kalbach: Phys.Rev.C37,2350(1988)


## Data Sections

| File | MT | Content | Records | Status |
|---|---|---|---|---|
| 1 | 451 | General info: Descriptive data and directory | 123 | Original |
| 3 | 2 | Cross sections: Elastic scattering | 22 | Original |
| 3 | 5 | Cross sections: All neutron channels (except elastic) | 22 | Original |
| 3 | 201 | Cross sections: (α,xn) — total neutron production | 393 | Supplement |
| 6 | 2 | Energy-angle distributions: Elastic scattering | 1,742 | Original |
| 6 | 5 | Energy-angle distributions: All neutron channels (except elastic) | 47,978 | Original |
| 6 | 201 | Energy-angle distributions: (α,xn) — total neutron production | 14,683 | Supplement |

---
