SELECT 
sb.name business_name,
 p.name AS perk_given, 
 p.status,
 p.starts,
 p.ends
FROM  perks p
JOIN small_businesses sb
    ON p.id = sb.id 
    
    
    