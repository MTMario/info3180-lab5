<template>

    <div v-if="success" class="s-alert">
        <h5> File has Successfully Uploaded </h5>
    </div>

    <div v-if="failure" class="f-alert">
        <ul>
            <li v-for="e in errormsg"> {{e}} </li>
        </ul> 
    </div>

    <form id="movieForm" @submit.prevent="saveMovie">

        <div class="form-group">
            <label for="title" class="form-label">Movie Title</label>
            <br>
            <input id="title" type="text" name="title" class="form-control"/>
            <br>
        </div>   
        <div class="form-group">
            <label for="description" class="form-label2"> Description </label>
            <br>
            <textarea id="desc" name="description" rows="5" cols="70"></textarea>
            <br>
        </div> 
        <div class="form-group3">
            <label for="poster" class="form-label3"> Image for Poster </label>
            <input id="img" type="file" name="poster"/>
            <br>
        </div>
        
        <br><button type="submit" value="submit"> Submit </button>
    
    </form>
</template>

<style>
    input[type="text"]{
        width: 400px;
        border-color:black;
    }
    .f-alert{
        width:600px;
        background-color: red;
        border-radius: 5px;
        padding-top:10px;
        padding-bottom:8px;
    }
    .s-alert{
        width:600px;
        background-color: #8CEF74;
        border-radius: 5px;
        padding-top:10px;
        padding-bottom:8px;
    }

    .form-label, .form-label2, .form-label3{
        padding-top:5px;
    }

    .form-label3 {
        padding-top: 4px;
        padding-right: 7px;
    }

    .form-group3{
        margin-top:17px;
        margin-left:10px;
        font-weight: bold;
    }

    .form-group{
        margin-left:10px;
        font-weight: bold;
    }

    button{
        background-color: #1E8CFB;
        margin-left:10px;
        border-radius: 5px;
        color:white;
        border-style:none;
        padding:10px;
    }
</style>

<script setup>
    import {ref, onMounted} from "vue";

    onMounted(() => {
    getCsrfToken();
    success.value = false;
    failure.value = false;
    })

    let csrf_token = ref("");
    let success = ref(false);
    let failure = ref(false);
    let errormsg = ref("");

    function getCsrfToken(){
        
        fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            })
    }

    function saveMovie(){
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {
            method:'POST',
            body: form_data,
            headers:{
                'X-CSRFTOKEN': csrf_token.value
            }
        })

        .then(function(response){
            return response.json();
        })

        .then(function(data){
            //display a success message
            let info = 0;
            for(info in data){errormsg = data[info];}
            if(document.getElementById('title').value == "" ||
            document.getElementById('desc').value == "" || 
            document.getElementById('img').value ==""){
                failure.value = true;
            }else{success.value = true}
        })

        .catch(function(error){
            console.log(error);
        });
    }

</script>