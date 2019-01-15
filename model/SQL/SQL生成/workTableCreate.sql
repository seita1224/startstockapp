CREATE TABLE stock_brand_wk (
  brand_wk_cd INT(4) NOT NULL,
  brand_wk_name VARCHAR(50),
  brand_wk_type VARCHAR(50),
  industry_wk_code_33_cd INT(4),
  industry_wk_code_33_name VARCHAR(50),
  industry_wk_code_17_cd INT(4),
  industry_wk_code_17_name VARCHAR(50),
  PRIMARY KEY (brand_wk_cd)
  ) ENGINE=INNODB;

