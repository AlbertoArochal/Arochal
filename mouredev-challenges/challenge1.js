const secondMax = () =>{
    const comparar = (a,b) =>{
        return b-a
    }; let argumentos = [arguments]
    let orderedL = argumentos.sort(comparar); return orderedL[1]
}

console.log(secondMax(1,2,3,4,5,6,7))