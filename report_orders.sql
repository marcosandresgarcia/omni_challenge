SELECT * FROM public.orders where status = 'DELIVERED' OR status = 'PENDING_SHIPPING'

SELECT * FROM public.shipments where status = 'PENDING'

SELECT orders.id as "id",orders.total_order_price as total_price,orders.status as "status",shipments.id as "id",
	shipments.address,shipments.cellphone_number,shipments.status as "shipment_status" INNER JOIN public.products_to_ship
	ON products_to_ship.shipment_id = shipments.id
	WHERE shipments.status = 'SHIPPED'

