let code=
{
	0:{
		name: "test",
		set: "=",
		int: 69420,
	},
}
const linecount=Object.keys(code).length;
for(let i = 0; i < linecount; i++){
	if(Object.keys(code[i])[1]=="set"){
		//set statement
	}
}