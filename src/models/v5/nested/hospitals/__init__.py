"""
//hospitals
new Thing("hospital",["doctor,2-4","nurse,2-4","intern,2-4","hospital room,3-8","patient,0-3","desk,0-2","chair,0-2",".building"]);
new Thing("hospital room",["doctor,10%","nurse,20%","intern,20%","bed,1-2","patient,0-2","tv","table,75%","chair,0-2",".room"]);
new Thing("nurse",[".Woman","Blood,10%"],"*WOMAN*| (nurse)");
new Thing("doctor",[".Person","Blood,5%"],"*PERSON*| (doctor)");
new Thing("intern",[".Person","Blood,10%"],"*PERSON*| (intern)");
new Thing("patient",[".Person","Blood,15%","wound,0-3"],"*PERSON*| (patient)");
"""
