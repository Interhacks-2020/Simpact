SELECT 
sb.name business_name,
 p.name AS perk_given, 
 p.status,
 p.starts,
 p.ends
FROM  perks p
JOIN small_businesses sb
<<<<<<< HEAD
    ON p.id = sb.id 
    
    
    
=======
    ON p.small_business_id = sb.id
>>>>>>> 313505b903ef8243be87ac19c1b8e649c839b227
