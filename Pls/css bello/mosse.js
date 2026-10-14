
function step(t, t0,t1) {
    let v = t<t0?0:t>t1?1:(t-t0)/(t1-t0);
    return (1-Math.cos(v*Math.PI))/2;
}

// scelgo che pezzo muovere e di quanti passi
// per i bianchi n_passi positivo è avanti, negativo indietro
// per i neri viceversa
function avanti(pezzo,z_partenza,n_passi,t,inizio,durata_mossa) {

    pezzo.pivot.position.z = z_partenza + n_passi * step(t,inizio, inizio + durata_mossa)

    /*
    if (t >= inizio && t <= inizio + durata_mossa) {
        pezzo.pivot.position.z = z_partenza + n_passi*(t-Math.floor(t));
    }
    if (t > inizio + durata_mossa) {
        pezzo.pivot.position.z = z_partenza + n_passi;
    }
    */
}



// scelgo che pezzo muovere e di quanti passi
// per i bianchi n_passi positivo è a destra, negativo sinistra
// per i neri viceversa
// destra e sinistra sono rispetto ai bianchi in basso
function laterale(pezzo,x_partenza,n_passi,t,inizio,durata_mossa) {
    if (t >= inizio && t <= inizio + durata_mossa) {
        pezzo.pivot.position.x = x_partenza + n_passi*(t-Math.floor(t));
    }
    if (t > inizio + durata_mossa) {
        pezzo.pivot.position.x = x_partenza + n_passi;
    }
}
// scelgo che pezzo muovere, di quanti passi e se verso destra o verso sinistra
// per i bianchi n_passi positivo è avanti, negativo indietro
// per i neri viceversa
// destra e sinistra sono rispetto ai bianchi in basso
function diagonale(pezzo,x_partenza,z_partenza,n_passi,direzione_x,t,inizio,durata_mossa) {
    passi_x = Math.abs(n_passi);
    if (t >= inizio && t <= inizio + durata_mossa) {
        if (direzione_x == "destra") {
            pezzo.pivot.position.z = x_partenza + n_passi * step(t,inizio, inizio + durata_mossa)

            pezzo.pivot.position.x = x_partenza + passi_x*(t-Math.floor(t));
        } else {
            pezzo.pivot.position.z = z_partenza + n_passi * step(t,inizio, inizio + durata_mossa)

            pezzo.pivot.position.x = x_partenza - passi_x*(t-Math.floor(t));
        }
        pezzo.pivot.position.z = z_partenza + n_passi*(t-Math.floor(t));
    }
    /*if (t > inizio + durata_mossa) {
        pezzo.pivot.position.z = z_partenza + n_passi;
        if (direzione_x == "destra") {
            pezzo.pivot.position.z = z_partenza + n_passi * step(t,inizio, inizio + durata_mossa)

            //pezzo.pivot.position.x = x_partenza + passi_x;
        } else {
            pezzo.pivot.position.z = z_partenza + n_passi * step(t,inizio, inizio + durata_mossa)

            //pezzo.pivot.position.x = x_partenza - passi_x;
        }
    }*/
}
// scelgo che pezzo muovere, "lungo/corto", "destra/sinista", "avanti/indietro"
// per i nero avanti/indietro funzionano al contrario
// destra e sinistra sono rispetto ai bianchi in basso
function salto(pezzo,x_partenza,z_partenza,tipo,direzione_x,direzione_z,t,inizio,durata_mossa){
    if (tipo == "lungo") {delta_z = 2; delta_x = 1;} else {delta_z = 1; delta_x = 2}
    if (direzione_x == "destra") {passi_x = delta_x} else {passi_x = -delta_x}
    if (direzione_z == "avanti") {passi_z = delta_z} else {passi_z = -delta_z}
    if (t >= inizio && t <= inizio + durata_mossa) {
        pezzo.pivot.position.x = x_partenza + passi_x*(t-Math.floor(t));
        pezzo.pivot.position.z = z_partenza + passi_z*(t-Math.floor(t));
        pezzo.pivot.position.y = 5 *(t-Math.floor(t)) * (1-t+Math.floor(t));
    }
    if (t > inizio + durata_mossa) {
        pezzo.pivot.position.z = z_partenza + passi_z;
        pezzo.pivot.position.x = x_partenza + passi_x;
        pezzo.pivot.position.y=0;
    }
}