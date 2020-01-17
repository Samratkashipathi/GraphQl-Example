# GraphQl-Example
GraphQl-Example

# Example 1
{  
  allUsers(name_Icontains: "samrat") {
    edges {
      node {
        id,
        name
      }
    }
  }
}

# Example 2

{
allPhotos {
  id,
  name,
  likes {
    edges {
      node {
        id,
        name,
        email
      }
    }
  }
}
}

# Example 3
mutation {
  createUser (name:"Sample 1", email: "sample@sample.com", age:22, friends:[1, 2,3 ,4]){
    name
  }
}


# Example 4
{
  allUsers {
    edges {
      node {
        id,
        name,
        friends {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}