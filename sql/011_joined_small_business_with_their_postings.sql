SELECT 
bp.business_name,
bp.description,
bp.age_requirements,
bp.points_available,
bp.logo

 
FROM business_posting bp
JOIN small_businesses sb
    ON bp.business_name = sb.id
    