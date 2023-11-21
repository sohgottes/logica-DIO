
// partidas rankeadas;

function partidasRankeadas(vitorias, derrotas){
    return totalPartidas = vitorias + derrotas;

}

let total = partidasRankeadas(77, 25);

console.log('total de partidas é' + total);

let saldoVitorias = (77-25);
let nivelHeroi

if (saldoVitorias < 10) {
    nivelHeroi = 'ferro';
} else if (saldoVitorias >= 11 && saldoVitorias <= 20) {
    nivelHeroi = 'bronze';
} else if (saldoVitorias >= 21 && saldoVitorias <= 50) {
    nivelHeroi = 'prata';
} else if (saldoVitorias >= 51 && saldoVitorias <= 80) {
    nivelHeroi = 'ouro';
} else if (saldoVitorias >= 81 && saldoVitorias <= 90) {
    nivelHeroi = 'diamante';
} else if (saldoVitorias >= 91 && saldoVitorias <= 100) {
    nivelHeroi = 'lendario';
} else {
    nivelHeroi = 'imortal';
}


console.log('o Herói tem um saldo de ' + saldoVitorias + 'está no nivel de ' + nivelHeroi + ' ');