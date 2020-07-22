SELECT 
<<<<<<< HEAD

=======
>>>>>>> 313505b903ef8243be87ac19c1b8e649c839b227
bp.business_name,
bp.description,
bp.age_requirements,
bp.points_available,
bp.logo

 
FROM business_posting bp
JOIN small_businesses sb
<<<<<<< HEAD
    ON bp.id = sb.id
=======
    ON bp.business_name = sb.id
>>>>>>> 313505b903ef8243be87ac19c1b8e649c839b227
    