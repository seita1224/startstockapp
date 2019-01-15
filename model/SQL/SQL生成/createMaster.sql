CREATE TABLE brand_type (
  brand_type_cd INT(4) NOT NULL,
  brand_type_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (brand_type_cd)
  ) ENGINE=INNODB;

CREATE TABLE industry_code_33 (
  industry_code_33_cd INT(4) NOT NULL,
  industry_code_33_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (industry_code_33_cd)
  ) ENGINE=INNODB;

CREATE TABLE industry_code_17 (
  industry_code_17_cd INT(4) NOT NULL,
  industry_code_17_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (industry_code_17_cd)
  ) ENGINE=INNODB;

CREATE TABLE stock_brand (
  brand_cd INT(4) NOT NULL,
  brand_name VARCHAR(50),
  brand_type_cd INT(4),
  industry_code_33_cd INT(4),
  industry_code_17_cd INT(4),
  PRIMARY KEY (brand_cd),
  FOREIGN KEY (brand_type_cd) REFERENCES brand_type(brand_type_cd),
  FOREIGN KEY (industry_code_33_cd) REFERENCES industry_code_33(industry_code_33_cd),
  FOREIGN KEY (industry_code_17_cd) REFERENCES industry_code_17(industry_code_17_cd)
  ) ENGINE=INNODB;