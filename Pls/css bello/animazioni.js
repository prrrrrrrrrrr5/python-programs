function giocoPiano(t) {
    document.getElementById("mosse").innerHTML="e4<span class='tab'></span>e5";
    avanti(PedoniBianchi[4],z_pedoni_bianchi,2,t,1,1);
    avanti(PedoniNeri[4],z_pedoni_neri,-2,t,2,1);
}
function gambettoDiRegina(t) {
    document.getElementById("mosse").innerHTML="d4<span class='tab'></span>d5 <br> c4";
    avanti(PedoniBianchi[3], z_pedoni_bianchi,2,t,1,1);
    avanti(PedoniNeri[3], z_pedoni_neri,-2,t,2,1);
    avanti(PedoniBianchi[2], z_pedoni_bianchi,2,t,3,1);
    
}    

function sicily(t){
    document.getElementById("mosse").innerHTML="e4<span class='tab'></span>c5 <br> Nf3<span class='tab'></span>Nc6 <br> d4";
    avanti( PedoniBianchi[4],z_pedoni_bianchi,2,t,1,1)
    avanti( PedoniNeri[2], z_pedoni_neri, -2, t, 2, 1)
    salto( cavalloG, x_primo_pezzo_bianco+6, z_nobili_bianchi, 'lungo', 'sinistra', 'avanti', t, 3, 1)
    salto( cavalloBn, x_primo_pezzo_nero+1, z_nobili_neri, 'lungo', 'destra', 'indietro', t, 4,1)
    avanti(PedoniBianchi[3], z_pedoni_bianchi, 2, t, 5, 1)
}    
function boh1(t) {
    avanti(PedoniBianchi[4],z_pedoni_bianchi,2,t,1,1);
    avanti(PedoniNeri[4],z_pedoni_neri,-2,t,2,1);
}

function boh2(t) {
    document.getElementById("mosse").innerHTML="e4<span class='tab'></span>c5";
    avanti(PedoniBianchi[4],z_pedoni_bianchi,2,t,1,1);
    avanti(PedoniNeri[2],z_pedoni_neri,-2,t,2,1);
}

function spagnola(t){
    document.getElementById("mosse").innerHTML="e4<span class='tab'></span>e5 <br> Cf3<span class='tab'></span>Cc6 <br> Ab5";
    avanti(PedoniBianchi[4],z_pedoni_bianchi,2,t,1,1)
    avanti(PedoniNeri[4],z_pedoni_neri,-2,t,2,1)
    salto(cavalloG,x_primo_pezzo_bianco+6,z_nobili_bianchi,'lungo','sinistra','avanti',t,3,1)
    salto(cavalloBn,x_primo_pezzo_nero+1,z_nobili_neri,'lungo','destra','indietro',t,4,1)
    diagonale(alfiereF,x_primo_pezzo_bianco+5,z_nobili_bianchi,4,'sinistra',t,5,1)
    
}

function slava(t){
    document.getElementById("mosse").innerHTML="d4<span class='tab'></span>d5 <br> c4<span class='tab'></span>c6";
    avanti(PedoniBianchi[3],z_pedoni_bianchi,2,t,1,1)
    avanti(PedoniNeri[3],z_pedoni_neri,-2,t,2,1)
    avanti(PedoniBianchi[2],z_pedoni_bianchi,2,t,3,1)
    avanti(PedoniNeri[2],z_pedoni_neri,-1,t,4,1)
}


function resetBoard() {
    PedoniBianchi.forEach(
        pedone => pedone.reset());
    PedoniNeri.forEach(
        pedone => pedone.reset());
    torreA.reset();
    torreAn.reset();
    torreH.reset();
    torreHn.reset();
    cavalloB.reset();
    cavalloBn.reset();
    cavalloG.reset();
    cavalloGn.reset();
    alfiereC.reset();
    alfiereCn.reset();
    alfiereF.reset();
    alfiereFn.reset();
    regina.reset();
    reginaN.reset();
    re.reset();
    reN.reset();
}

function mostraApertura(apertura) {
    aperturaAttiva = apertura;
    resetBoard();
    startTime = performance.now() * 0.001;
}