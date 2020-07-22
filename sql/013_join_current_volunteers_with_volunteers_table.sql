SELECT 
cv.id,
cv.first_name,
cv.last_name,
cv.points_earned,
cv.location


FROM current_volunteers cv
JOIN volunteers v
    ON cv.id = v.id