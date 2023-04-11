<script setup>
 import { ref, onMounted } from "vue";
    let mov = ref([]);
    onMounted(() => {
        fetchMovies()
    })

    function fetchMovies(){
    
    fetch('/api/v1/movies',{
        method:'GET'
    })
      .then(function(response) {
        return response.json();
        })
      .then(function(data) {
        mov.value = data.mov;
      })
      .catch(function(error){
         console.log(error);
      })
    }
</script>


<template>
        <h2 class="head"> Movies </h2>
        <div class="cards">
            <div v-for="movie in mov" class="card">
                <div class="image">
                    <img :src="movie.poster"/>
                </div>
                <div class="content">
                    <h3> {{movie.title}} </h3>
                    <p> {{movie.description}} </p>
                </div>
            </div>
        </div>
</template>

<style>
.cards {
    display: flex;
    flex-wrap: wrap;
}
  
.card {
    display: flex;
    flex-direction: row;
    border-radius: 7px;
    width: 560px;
    margin-right:70px;
    margin-left:50px;
    margin-bottom: 10px;
}

.head{
    margin-left:50px;
}

img {
    width: 200px;
    height: 280px;
}

.content{
    flex: 1 1 auto;
    margin-left:15px;
    margin-right:7px;
}

.content h3 {
    margin-top: 10px;
}

.content p {
    margin-top: -7px;
    font-weight:500;
}
</style>