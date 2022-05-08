let code={inject: "/code-string"}
const linecount=Object.keys(code).length;
for(let i = 0; i < linecount; i++){
    for(let j = 0; j < Object.keys(code[i]).length; j++){
        let key = Object.keys(code[i])[j];
		console.log(key,code[i][key]);
	}
}