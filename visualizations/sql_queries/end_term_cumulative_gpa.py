def get_query(from_time, to_time, substr):

    return "SELECT gpa.end_term_cumulative_gpa, count(gpa.end_term_cumulative_gpa) FROM visits LEFT JOIN gpa ON visits.student_id = gpa.student_id where (location = \'" + substr + "\') and check_in_date >= \'" + from_time + "\' and check_in_date <= \'" + to_time + "\' and gpa.end_term_cumulative_gpa is not null group by gpa.end_term_cumulative_gpa;"