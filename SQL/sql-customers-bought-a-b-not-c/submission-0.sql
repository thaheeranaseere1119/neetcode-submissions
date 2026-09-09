-- Write your query below
select distinct(o.customer_id),c.customer_name from customers c
 join orders o on c.customer_id=o.customer_id 
 where o.customer_id not in(select o.customer_id from orders o where o.product_name ='C')and 
 o.customer_id in(select o.customer_id from orders o where o.product_name ='A')and 
 o.customer_id in(select o.customer_id from orders o where o.product_name='B') order by c.customer_name