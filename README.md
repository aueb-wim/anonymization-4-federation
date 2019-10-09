# anonymization-4-federation
Anonymizing data by hashing id's while using randomly generated numbers

The current module deletes the id's of a relational i2b2-schema database while preserving the entities' resolution and relationships among them. Having as input an i2b2 database, the output is a replicated database with randomly generated patient and encounter id's which are not possible to be linked to the input db's id's. This applies in both ways, meaning the output id's cannot be re-generated in the same way therefore cannot be linked to those of an already anonymized database. To succeed that, we add to each id a random_number from 1 to 100 and then we hash it.

new_id = MD5(id + random_number) or 
new_id = SHA3_224(id + random_number)

For the case where the data are already in CSV we randomly hash the id column.

Currently the hashing function that is being used is MD5 and SHA3-224. In the future we may use others like SHA256, SHA512. Postgres provides several crypto functions (https://www.postgresql.org/docs/9.4/pgcrypto.html), therefore MD5 can be easily replaced by a more secure one. On the other hand, even if someone manages to decrypt (dehash) she will get the sum of the id and a random_number and not the id itself.

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
