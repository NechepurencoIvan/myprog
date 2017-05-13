--DROP TABLE donors;
--DROP TABLE ill;
--DROP TABLE donors_ill;
--DROP TABLE persons;
CREATE TABLE persons (
    person_id INT NOT NULL,
    fam TEXT NOT NULL,
    name TEXT NOT NULL,
    otch TEXT,
    contact_id INT NOT NULL,
    PRIMARY KEY(person_id)
    );
CREATE TABLE donors (
    donor_id int NOT NULL,
    person_id int NOT NULL,
    bllood_gr int NOT NULL CHECK (bllood_gr = '1' OR bllood_gr = '2' OR bllood_gr = '3' OR bllood_gr = '4' OR),
    rf boolean NOT NULL,
    born date NOT NULL,
    sex text,
    work text,
    passed int,
    lastpass date,
    PRIMARY KEY(person_id)
);
CREATE TABLE ill (
    ill_id int NOT NULL,
    person_id int NOT NULL,
    bllood_gr int NOT NULL CHECK (bllood_gr = '1' OR bllood_gr = '2' OR bllood_gr = '3' OR bllood_gr = '4' OR),
    rf boolean NOT NULL,
    disease text NOT NULL,
    volume int NOT NULL,
    PRIMARY KEY(person_id)
);
CREATE TABLE donors_ill (
    donor_id int NOT NULL,
    ill_id int NOT NULL,
    confirm bool NOT NULL,
    PRIMARY KEY(person_id)
);

CREATE TABLE hashes(
    contact_id int CHECK(contact_id < '10000')
    hash TEXT
    PRIMARY KEY(contact_id)
);
--SELECT * FROM donors, ill, donors_ill;