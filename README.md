# anonymization-4-federation
Anonymizing data by hashing id's while using randomly generated numbers

The current module deletes the id's of a relational i2b2-schema database while preserving the entities' resolution and relationships among them. Having as input an i2b2 database, the output is a replicated database with randomly generated object and encounter id's which are not possible to be linked to the input db's id's. This applies in both ways, meaning the output id's cannot be re-generated in the same way therefore cannot be linked to those of an output id.

There is an option to choose between MD5 and SHA1 hashing functions.
