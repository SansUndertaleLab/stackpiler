let code=
{
	0:{
		name_1: "test",
		set_2: "=",
		int_3: 1,
		add_4: "+",
		int_5: 2,
		add_6: "+",
		int_7: 3,
	},
	1:{
		name_1: "test2",
		set_2: "=",
		name_3: "test",
		mul_4: "*",
		int_5: 2,
	},
}
const linecount=Object.keys(code).length;
for(let i = 0; i < linecount; i++){
    for(let j = 0; j < Object.keys(code[i]).length; j++){
        let key = Object.keys(code[i])[j];
		console.log(key,code[i][key]);
	}
}