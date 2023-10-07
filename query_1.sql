insert into order_items_customer_a 
select
    order_item_id,
    order_item_order_id,
    order_item_product_id,
    order_item_quantity,
    order_item_subtotal,
    order_item_product_price,
    order_date,
    order_customer_id,
    order_status,
    customer_fname,
    customer_lname,
    customer_state,
    customer_zipcode,
    product_name,
    category_name,
    department_name,
	replace(';',' ',department_name)
from order_items_customer WHERE year = '2023';