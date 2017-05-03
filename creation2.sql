CREATE TABLE persons (person_id int, fam text, name text, otch text, contact_id int);
CREATE TABLE donors (donor_id int,person_id int, bllood_gr int, rf boolean,born date, sex text,work text, passed int, lastpass date);
CREATE TABLE ill (ill_id int, person_id int, bllood_gr int, rf boolean, disease text,volume int);
CREATE TABLE donors_ill (donor_id int, ill_id int, confirm bool);