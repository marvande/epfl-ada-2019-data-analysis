# Notes on the dunnhumby datasets we're gonna use: 
## Note : 
total of 2500 households but only demographic data for 801 households. 

## hh-demographic: 
demographic info for a certain portion of households. 

Attributes: 
- HOUSEHOLD_KEY : identifies each household, unique
- AGE_DESC: estimated age range
- MARITAL_STATUS_CODE: A -> Married, B -> Single, C -> Unknown
- INCOME_DESC : Household income
- HOMEOWNER_DESC: Homeowner, renter, etc
- HH_COMP_DEC: Household composition
- HOUSEHOLD_SIZE_DESC: Size of household up to 5+ 
- KID_CATEGORY_DESC: Number of children present up to 3+ 


## transaction_data: 
all products purchased by households during the study. Each line in the table is what could essentially be found in a store reciept. 

Attributes: 

- HOUSEHOLD_KEY: identifies each household, unique
- BASKET_ID: identifies a purchase occasion, unique
- DAY: day when transaction occured
- PRODUCT_ID: identifies each product, unique
- QUANTITY: Number of products purchased during trip
- SALES_VALUE: Amount of dollars retailer recieves from sale
- STORE_ID: identifies store, unique
- COUPON_MATCH_DISC: discount applied du to retailer's match of manufacturer coupon
- COUPON_DISC: discount applied due to manufacturer coupon
- RETAIL_DISC: discount applied due to retailer's loyalty card program
- TRANS_TIME: time of day when transaction occured
- WEEK_NO: week of the transaction. Ranges from 1-102. 

## product: 
information on each product sold such as type of product, national or private label and a brand identifier. 

Attributes: 
- PRODUCT_ID: unique, identifies product
- DEPARMENT: groups similar products together
- COMMODITY_DESC: groups similar products together at a lower level
- SUB_COMMODITY_DESC: groups similar products together at the lowest level
- MANUFACTURER: code that links products with the same manufacturer together 
- BRAND: indicates private or national label brand
- CURR_SIZE_OF_PRODUCT: indicates package size (not available for all) 

## updated_prod_precise:
clean version of product, the products are labeled in 32 different categories.

## trans_clean:
clean version of transaction_data, useless departments are discarded.

## hh_demographic_fix_hhcomp:
fixed version of hh-demographic.
- HOUSEHOLD_KEY : identifies each household, unique
- AGE_DESC: estimated age range
- MARITAL_STATUS_CODE: M -> Married, S -> Single
- INCOME_DESC : Household income
- HOMEOWNER_DESC: Homeowner, renter, etc
- HOUSEHOLD_SIZE_DESC: Size of household up to 5+
- KIDS_DESC: Number of children present up to 3+

## hh_spendig:
demographic data frame where we add mean yearly budget and mean weekly budget
- hh_demographic_fix_hhcomp COLUMNS
- mean weekly spending
- mean yearly spending

## weekly_cart_df:
dataframe with household ID and weekly purchase frequencies for every product LABEL
- HOUSEHOLD_KEY
- PRODUCE_QUANT
- HOUSEHOLDS_QUANT
- CONDIMENTS_QUANT
...
