# tar -czvf archive.tar.gz file1 file2 file3    - запаковать
# tar -cjvf archive.tar.bz2 file1 file2 file3   - запаковать

# tar -xzvf archive.tar.gz  - распаковать
# tar -xjvf archive.tar.bz2 - распаковать
cd ./stage_2_data/
tar -czvf  B.tar.gz     B/
tar -czvf Be.tar.gz     Be/
tar -czvf  C.tar.gz     C/
tar -czvf Li.tar.gz     Li/
tar -czvf  N.tar.gz     N/

tar -cvjf  O.tar.bz2    O/
tar -cvjf Na.tar.bz2    Na/
tar -cvjf  F.tar.bz2    F/