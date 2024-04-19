DROP TABLE IF EXISTS "public"."items" CASCADE;
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Create the first table.
CREATE TABLE "public"."items"(
  "id" SERIAL PRIMARY KEY,
  "item_name" text,
  "price" int,
  "stock_quantity" int
);

DROP TABLE IF EXISTS "public"."items_orders" CASCADE;
-- Create the join table.
CREATE TABLE "public"."items_orders"(
  "item_id" int,
  "order_id" int
);

DROP TABLE IF EXISTS "public"."orders" CASCADE;
-- Create the second table.
CREATE TABLE "public"."orders"(
  "id" SERIAL PRIMARY KEY,
  "customer_name" text,
  "order_date" date
);

INSERT INTO "public"."items"("item_name", "price", "stock_quantity") VALUES
('Dog treats', 5, 50),
('Dog Collars', 25, 42),
('Dog beds', 75, 23),
('Dog food', 70, 1),
('Dog toys', 20, 32),
('Dog blankets', 15, 56),
('Dog shirts', 35, 65),
('Paw Cleaner', 30, 48),
('Dog Shampoo', 15, 96);

INSERT INTO "public"."orders"("customer_name", "order_date") VALUES
('Anna' , '2024-05-19'),
('Rachel', '2024-05-19'),
('Tom', '2024-08-23'),
('John', '2024-02-14'),
('Thomas', '2024-06-18'),
('Paul', '2024-01-19'),
('Steve', '2024-07-12'),
('Hunor', '2024-06-11'),
('Eoin', '2024-08-26'),
('Jen', '2024-03-29'),
('Selva', '2024-02-15');

INSERT INTO "public"."items_orders"("item_id", "order_id") VALUES
(1, 1),
(1, 11),
(2, 10),
(3, 9),
(9, 8),
(8, 7),
(7, 5),
(6, 4),
(5, 3),
(6, 2),
(7, 1),
(6, 3),
(2, 4),
(3, 8);

ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("item_id") REFERENCES "public"."items"("id");
ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("order_id") REFERENCES "public"."orders"("id");

