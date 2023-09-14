# anonymization-4-federation
Anonymizing data by hashing id's while using randomly generated numbers

This process is designed in the context of the Data Factory pipeline for the Medical Informatics Platform of the Human Brain Project.
The current process deletes the id's of a relational i2b2-schema database while preserving the entities' resolution and relationships among them. Having as input an i2b2 database, the output is a replicated database with randomly generated patient and encounter id's which are not possible to be linked to the input db's id's. This applies in both ways, meaning the output id's cannot be re-generated in the same way therefore cannot be linked to those of an already anonymized database. To succeed that, we add to each id a random_number from 1 to 100 and then we hash it.

new_id = MD5(id + random_number) or 
new_id = SHA3_224(id + random_number)

For the case where we have NOT used the Data Factory and the data are already in a CSV file, we randomly hash the id column with a python script.

The hashing function that is used is MD5 or SHA3-224. We may use others like SHA3-256, SHA3-512. Postgres (as well as python) provides several crypto functions (https://www.postgresql.org/docs/9.4/pgcrypto.html), therefore we can easily choose the one we prefer and consider to be more secure. 
Keep in mind that even if someone manages to decrypt (de-hash) she will get the sum of the id and a random_number and not the id itself; therefore even in that extreme scenario there will be no linkage to the original tuple via the id.

## Python script usage
Give the command in terminal
```shell
./anonymize_csv.py <inputcsvpath> <outputcsvpath>
```
**Options**

- `-c` or `--columns` -
By default the script will hash the first column of the input csv. If we want to hash certain columns, i.e. 2nd and 3rd column, we add `-c 2 3` or `--columns 2 3`.

- `-m` or `--method` -
The hash function that will be used. Select between `md5` and `sha3`. As default is the `sha3` method.

## Acknowledgements
This project/research received funding from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Framework Partnership Agreement No. 650003 (HBP FPA).
