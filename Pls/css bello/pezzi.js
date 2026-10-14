const NERO = "nero";
const BIANCO = "bianco";
let materialeBianchi, materialeNeri;

class Pedone{
    constructor(squadra, startx=0, startz=0) {
        this.squadra = squadra;
        this.startx = startx;
        this.startz = startz;
      
        let materiale = this.squadra == NERO ? materialeNeri : materialeBianchi;

        let pivot = this.pivot = new BABYLON.TransformNode('p', scene);
        pivot.position.set(startx,0,startz);
        
        let base = BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.7, 
            thickness: 0.14, 
            tessellation: 40
        },scene);
        base.parent = pivot;
        base.position.y = 0.07;
        base.material = materiale;
        
        let corpo = BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.15, 
            diameterBottom: 0.7, 
            height: 0.8
        },scene);
        corpo.parent = base
        corpo.position.y = 0.47
        corpo.material = materiale;

        let testa = BABYLON.MeshBuilder.CreateSphere('sphere',{
            diameter: 0.4
        },scene);
        testa.parent = corpo;
        testa.position.y = 0.4;
        testa.material = materiale;

        
    }

    reset() {
        this.pivot.position.set(this.startx, 0, this.startz);
    }
}

class Regina{
    constructor(squadra, startx=0, startz=0) {
        this.squadra = squadra;
        this.startx = startx;
        this.startz = startz;
        let materiale = this.squadra == NERO ? materialeNeri : materialeBianchi;

        let pivot = this.pivot = new BABYLON.TransformNode('p', scene);
        pivot.position.set(startx,0,startz);

        let base= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.8, 
            thickness: 0.2, 
            tessellation: 40
        },scene);
        base.parent = pivot;
        base.position.y = 0.1;
        base.material = materiale;
        
        let corpo= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.2, 
            diameterBottom: 0.8, 
            height: 1.3
        },scene);
        corpo.parent = base;
        corpo.position.y = 0.7;
        corpo.material = materiale;
 
        let testa= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.6, 
            diameterBottom: 0.2, 
            height: 0.6
        },scene);
        testa.parent = base;
        testa.position.y = 1.65;
        testa.material = materiale;
        
        let colletto=BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.2, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        colletto.parent = testa;
        colletto.position.y = -0.3;
        colletto.material = materiale;

        let corona=BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.5, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        corona.parent = testa;
        corona.position.y = 0.3;
        corona.material = materiale;

        let copricorona=BABYLON.MeshBuilder.CreateSphere('sphere',{
            diameter:0.5
        },scene);
        copricorona.parent = corona;
        copricorona.position.y = 0;
        copricorona.material = materiale;

        let punta=BABYLON.MeshBuilder.CreateSphere('sphere',{
            diameter:0.2
        },scene);
        punta.parent = copricorona;
        punta.position.y = 0.3;
        punta.material = materiale;

    }

    reset() {
        this.pivot.position.set(this.startx, 0, this.startz);
    }
}

class Re{
    constructor(squadra, startx=0, startz=0) {
        this.squadra = squadra;
        this.startx = startx;
        this.startz = startz;
        let materiale = this.squadra == NERO ? materialeNeri : materialeBianchi;
 
        let pivot = this.pivot = new BABYLON.TransformNode('p', scene);
        pivot.position.set(startx,0,startz);

        let base= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.8, 
            thickness: 0.2, 
            tessellation: 40
        },scene);
        base.parent = pivot;
        base.position.y = 0.1;
        base.material = materiale;

        let corpo= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.2, 
            diameterBottom: 0.8, 
            height: 1.5
        },scene);
        corpo.parent = base;
        corpo.position.y = 0.7;
        corpo.material = materiale;

        let testa= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.6, 
            diameterBottom: 0.2, 
            height: 0.6
        },scene);
        testa.parent = base;
        testa.position.y = 1.8;
        testa.material = materiale;

        let mezzo=BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.6, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        mezzo.parent = corpo;
        mezzo.position.y = 0;
        mezzo.material = materiale;

        let colletto=BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.2, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        colletto.parent = testa;
        colletto.position.y = -0.3;
        colletto.material = materiale;

        let corona=BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.5, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        corona.parent = testa;
        corona.position.y = 0.3; 
        corona.material = materiale;

        let ciaffo= BABYLON.MeshBuilder.CreateBox('box',{
            width:0.2, height:0.4, depth:0.1
        },scene);     
        ciaffo.parent = corona;
        ciaffo.position.y = 0.2;
        ciaffo.material = materiale;

        let ciaffo1= BABYLON.MeshBuilder.CreateBox('box',{
            width:0.4, height:0.2, depth:0.1
        },scene);    
        ciaffo1.parent = ciaffo;
        ciaffo1.position.y = 0;
        ciaffo1.material = materiale;

    }

    reset() {
        this.pivot.position.set(this.startx, 0, this.startz);
    }
}

class Torre{
    constructor(squadra, startx=0, startz=0) {
        this.squadra = squadra;
        this.startx = startx;
        this.startz = startz;
        let materiale = this.squadra == NERO ? materialeNeri : materialeBianchi;

        let pivot = this.pivot = new BABYLON.TransformNode('p', scene);
        pivot.position.set(startx,0,startz);

        let base= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.8, 
            thickness: 0.16, 
            tessellation: 40
        },scene);
        base.parent = pivot;
        base.position.y = 0.08;
        base.material = materiale;

        let base2= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.6, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        base2.parent = base;
        base2.position.y = 0.1;
        base2.material = materiale;
        
        let corpo= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameter: 0.6, 
            height: 1.3
        },scene);
        corpo.parent = base;
        corpo.position.y = 0.7;
        corpo.material = materiale;
        
        let merli= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.6, 
            thickness: 0.15, 
            tessellation: 40
        },scene);
        merli.parent = base;
        merli.position.y = 1.4;
        merli.material = materiale;

    }

    reset() {
        this.pivot.position.set(this.startx, 0, this.startz);
    }
}

class Cavallo{
    constructor(squadra, startx=0, startz=0, rotation=0) {
        this.squadra = squadra;
        this.startx = startx;
        this.startz = startz;
        this.rotation = rotation;
        let materiale = this.squadra == NERO ? materialeNeri : materialeBianchi;

        let pivot = this.pivot = new BABYLON.TransformNode('p', scene);
        pivot.position.set(startx,0,startz);
        pivot.rotation.set(0,rotation,0);

        let base= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.8, 
            thickness: 0.16, 
            tessellation: 40
        },scene);
        base.parent = pivot;
        base.position.y = 0.08;
        base.material = materiale;

        let corpo= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterBottom:0.8,
            diameterTop:0.1, 
            height:1
        },scene);
        corpo.parent = base;
        corpo.position.y = 0.58;
        corpo.material = materiale;

        let testa= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop:0.4, 
            diameterBottom:0.2, 
            height:0.6
        },scene);
        testa.parent = corpo;
        testa.rotation.x = -Math.PI/4;
        testa.position.y = 0.5;
        testa.position.z = 0.2;
        testa.material = materiale;

        // per posizionare simmetricamente le due orecchie
        let dt = 0.05;
        let db = 0.15;
        let ho = 0.15;
        let xo = 0.09;
        let yo = 0.38;
        let zo = 0.09;

        let orecchio1= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: dt, 
            diameterBottom: db, 
            height: ho
        },scene);
        orecchio1.parent = testa;
        orecchio1.position.x = xo;
        orecchio1.position.y = yo;
        orecchio1.position.z = zo;
        orecchio1.material = materiale;

        let orecchio2= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: dt, 
            diameterBottom: db, 
            height: ho
        },scene);
        orecchio2.parent = testa;
        orecchio2.position.x = -xo;
        orecchio2.position.y = yo;
        orecchio2.position.z = zo;
        orecchio2.material = materiale;

    }

    reset() {
        this.pivot.position.set(this.startx, 0, this.startz);
    }
}

class Alfiere{
    constructor(squadra, startx=0, startz=0) {
        this.squadra = squadra;
        this.startx = startx;
        this.startz = startz;
        let materiale = this.squadra == NERO ? materialeNeri : materialeBianchi;

        let pivot = this.pivot = new BABYLON.TransformNode('p', scene);
        pivot.position.set(startx,0,startz);

        let base= BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.8, 
            thickness: 0.16, 
            tessellation: 40
        },scene);
        base.parent = pivot;
        base.position.y = 0.08;
        base.material = materiale;

        let corpo= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.4, 
            diameterBottom: 0.8, 
            height: 1
        },scene);
        corpo.position.y = 0.4;
        corpo.parent = base;
        corpo.material = materiale;

        let colletto=BABYLON.MeshBuilder.CreateTorus('torus',{
            diameter: 0.4, 
            thickness: 0.16, 
            tessellation: 40
        },scene);
        colletto.parent = corpo;
        colletto.position.y = 0.58;
        colletto.material = materiale;

        let testa= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameter: 0.4, 
            height: 0.08
        },scene);
        testa.parent = colletto;
        testa.position.y = 0.12;
        testa.material = materiale;

        let testa1= BABYLON.MeshBuilder.CreateCylinder('cone',{
            diameterTop: 0.1, 
            diameterBottom: 0.4, 
            height: 0.2
        },scene);
        testa1.position.y = 0.14;
        testa1.parent = testa;
        testa1.material = materiale;

        let punta=BABYLON.MeshBuilder.CreateSphere('sphere',{
            diameter:0.2
        },scene);
        punta.parent = testa1;
        punta.position.y = 0.2;
        punta.material = materiale;
        
    }

    reset() {
        this.pivot.position.set(this.startx, 0, this.startz);
    }
}