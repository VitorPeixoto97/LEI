<template>
    <div>
        <form id="clube" @submit.prevent="onSubmit">
            Nome do clube: <input v-model="nome" lazy placeholder="Nome" required>
            <hs>
            Cor da equipa: <input v-model="cor" lazy placeholder="Cor" required>
            <hs>
            Símbolo da equipa: <input type="file" @change="onFileChanged" accept="image/*" required>
            <hs>
            <input type="submit" value="Submit">
        </form>
    </div>
</template>

<script>
</script>

<style>
</style>