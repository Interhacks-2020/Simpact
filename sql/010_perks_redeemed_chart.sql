SELECT 
v.first_name, 
v.last_name,
p.name AS perk_redeemed,
sb.name AS location,
v.points - p.point_price AS point_balance,
v.perk_date AS date
FROM volunteers v
JOIN perks p
   ON v.id = p.id
JOIN small_businesses sb
   ON v.id = sb.id 