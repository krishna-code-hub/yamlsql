with categories_dept as (
select * from {{source('t1_source','categories')}} 
left join {{source('t1_source','departments')}} 
on category_department_id == department_id
),

order_items_product as (
select * from {{source('t1_source','order_items')}} 
left join {{source('t1_source','products')}} 
on order_item_product_id == product_id
),

order_items_product_dept as (
select * from order_items_product
left join categories_dept
on order_items_product.product_category_id == categories_dept.category_id
)
select * from order_items_product_dept WHERE ods = '2023_01_01';