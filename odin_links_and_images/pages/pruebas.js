
cosites = [['potito', 'manrrique', 'casucha', 'flaquito', 'ringo'], ['george', 'guarapo', 'maquito', 'Paul'], ['john', 'sarita']]
let beatles = []
for (let i = 0; i < cosites.length; i++) {
    for (let j = 0; cosites[i].length; j++) {
        switch (cosites[i][j]) {
            case 'ringo':
                beatles.push(cosites[i][j])
                break
            case 'george':
                beatles.push(cosites[i][j])
                break
            case 'Paul':
                beatles.unshift(cosites[i][j])
                break
            case 'john':
                beatles.unshift(cosites[i][j])
                break
                

        }

    }
}
console.log(beatles)