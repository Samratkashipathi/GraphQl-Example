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