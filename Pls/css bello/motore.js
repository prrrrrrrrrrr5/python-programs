'use strict';
let canvas, engine, scene, camera;
window.addEventListener('DOMContentLoaded', () => {
    // il tag canvas che visualizza l'animazione
    canvas = document.getElementById('c');
    // la rotella del mouse serve per fare zoom e non per scrollare la pagina
    canvas.addEventListener('wheel', evt => evt.preventDefault());
    // engine & scene
    engine = new BABYLON.Engine(canvas, true);
    scene = new BABYLON.Scene(engine);    
    // camera
    camera = new BABYLON.ArcRotateCamera('cam', 
            -Math.PI/4,0.7,16,  //-Math.PI/2,0.7,15,
            new BABYLON.Vector3(0.2,0.2,0.2), 
            scene);
    camera.attachControl(canvas,true);
    camera.wheelPrecision = 50;
    camera.lowerRadiusLimit = 3;
    camera.upperRadiusLimit = 13*2;            
    // luce
    let light1 = new BABYLON.PointLight('light1',new BABYLON.Vector3(0,1,0), scene);
    light1.parent = camera;

    // musica ??
        
    // aggiungo i vari oggetti
    populateScene(scene);
    // main loop
    engine.runRenderLoop(()=>scene.render());
    // resize event
    window.addEventListener("resize", () => engine.resize());
});

let startTime = 0;
let aperturaAttiva = null;

let PedoniBianchi, PedoniNeri, torreA, torreAn, torreH, torreHn, cavalloB, cavalloBn, cavalloG, cavalloGn, alfiereC, alfiereCn, alfiereF, alfiereFn, regina, reginaN, re, reN;

// pezzi bianchi
// posizione su x del primo pezzo bianco
let x_primo_pezzo_bianco = -3.5;
// posizione su z dei pedoni bianchi
let z_pedoni_bianchi  = -2.5;
// posizione su z degli altri pezzi bianchi
let z_nobili_bianchi = -3.5;

//pezzi neri   
// posizione su x del primo pezzo nero
let x_primo_pezzo_nero=-3.5;
// posizione su z dei pedoni neri
let z_pedoni_neri = 2.5;
// posizione su z degli altri pezzi neri
let z_nobili_neri = 3.5;


function populateScene() {   
    //createGrid(scene);
    //colore sfondo
    scene.clearColor = new BABYLON.Color3(0.933,0.933,0.933); //celeste

    // la base su cui appoggia la scacchiera
    let base = new BABYLON.MeshBuilder.CreateBox('box', {height: 0.4, width: 10, depth: 10},scene);
    base.material = new BABYLON.StandardMaterial('materiale-base', scene);
    base.material.diffuseColor.set(0.04,0.21,0.54); //blue
    //base.material.specularColor.set(0.2,0.2,0.2);
    base.position.y=-0.4;
    // la scacchiera
    let cont=0    
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            let piano=new BABYLON.MeshBuilder.CreateBox('box', {height: 0.2, width: 1, depth: 1},scene);
            piano.position.x = i-3.5;
            piano.position.y = -0.1;
            piano.position.z = j-3.5;
            piano.material = new BABYLON.StandardMaterial('matsca', scene);
            if (cont%2==0) {
                piano.material.diffuseColor.set(0,0,0); //caselle nere
                //piano.material.specularColor.set(0.2,0.2,0.2);
            } else {
                piano.material.diffuseColor.set(1,1,1); //caselle bianche
                //piano.material.specularColor.set(0.2,0.2,0.2);
            }
            cont++;
        }
        cont++;
    }
    

    // scelgo i colori per i pezzi bianchi e i pezzi neri
    materialeBianchi = new BABYLON.StandardMaterial('mat', scene);
    materialeBianchi.diffuseColor.set(0.88,0.76,0.33); //gold
    materialeNeri = new BABYLON.StandardMaterial('mat', scene);
    materialeNeri.diffuseColor.set(0.55,0.04,0.18); //red


    PedoniBianchi = [];
    for (let m = -3.5; m < 4.5; m++) {
        let pedone= new Pedone(BIANCO, m, -2.5);
        PedoniBianchi.push(pedone);        
    }
    torreA= new Torre(BIANCO, x_primo_pezzo_bianco, z_nobili_bianchi);

    cavalloB = new Cavallo(BIANCO, x_primo_pezzo_bianco + 1, z_nobili_bianchi);

    alfiereC = new Alfiere(BIANCO, x_primo_pezzo_bianco +2, z_nobili_bianchi);
   
    regina = new Regina(BIANCO, x_primo_pezzo_bianco + 3, z_nobili_bianchi);

    re = new Re(BIANCO, x_primo_pezzo_bianco + 4, z_nobili_bianchi);
    
    alfiereF = new Alfiere(BIANCO, x_primo_pezzo_bianco + 5, z_nobili_bianchi);
     
    cavalloG = new Cavallo(BIANCO, x_primo_pezzo_bianco + 6, z_nobili_bianchi);

    torreH= new Torre(BIANCO, x_primo_pezzo_bianco + 7, z_nobili_bianchi);


    
    PedoniNeri= [];
    for (let m = -3.5; m < 4.5; m++) {
        PedoniNeri.push(new Pedone(NERO, m, 2.5))   
    }

    torreAn= new Torre(NERO, x_primo_pezzo_nero, z_nobili_neri);

    cavalloBn = new Cavallo(NERO, x_primo_pezzo_nero + 1, z_nobili_neri, -Math.PI);

    alfiereCn = new Alfiere(NERO, x_primo_pezzo_nero + 2, z_nobili_neri);

    reginaN = new Regina(NERO, x_primo_pezzo_nero + 3, z_nobili_neri);

    reN= new Re(NERO, x_primo_pezzo_nero + 4, z_nobili_neri);

    alfiereFn = new Alfiere(NERO, x_primo_pezzo_nero + 5, z_nobili_neri);

    cavalloGn = new Cavallo(NERO, x_primo_pezzo_nero + 6, z_nobili_neri, -Math.PI);

    torreHn= new Torre(NERO, x_primo_pezzo_nero + 7, z_nobili_neri);



    scene.registerBeforeRender(() => {
        let t = performance.now() * 0.001;

        if(aperturaAttiva != null) 
            aperturaAttiva(t - startTime);

   });   
}