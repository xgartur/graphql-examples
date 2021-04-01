const axios = require('axios')
require('dotenv').config({ path: '../.env' })

console.log("URL",process.env.TOKEN)
console.log("TOKEN",process.env.GRAPHQL_URL)

async function main(){
  const query = `
      {
        usuarios{
          id
          usuariosnuevos
          usuariosactivos
          usuariosregistrados
        }
      }
      `
  const data = await axios({
    url: process.env.GRAPHQL_URL,
    method: 'post',
    data: {
      query
    }
  })
  console.log(data.data)
}


main()
