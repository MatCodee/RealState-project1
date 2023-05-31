// select Information:
const chile_places = [
    {
        region: 'Arica y Parinacota',
        places: [
            'todo',
            'Arica',
            'Parinacota',
            'Putre',
        ]
    },
    {
        region: 'Tarapaca',
        places: [
            'todo',
            'Alto Hospicio',
            'Iquique',
            'Pozo Almonte',
        ]
    },
    {
        region: 'Antofagasta',
        places: [
            'todo',
            'Antofagasta',
            'Calama',
            'María Elena',
            'Mejillones',
            'San Pedro',
            'Taltal',
            'Tocopilla'
        ]
    },
    {
        region: 'Atacama',
        places: [
            'todo',
            'Caldera',
            'Chañaral',
            'Copiapó',
            'Diego De Almagro',
            'Salvador',
            'Huasco',
            'Tierra Amarilla',
            'Vallenar',
        ]
    },
    {
        region: 'Coquimbo',
        places: [
            'todo',
            'Andacollo',
            'Combarbalá',
            'Coquimbo',
            'Palqui',
            'Illapel',
            'La Serena',
            'Los Vilos',
            'Monte Patria',
            'Ovalle',
            'Salamanca',
            'Vicuña'
        ]
    },
    {
        region: 'Valparaíso',
        places: [
            'todo',
            'Algarrobo',
            'Cabildo',
            'Calle Larga',
            'Cartagena',
            'Casablanca',
            'Catemu',
            'Concón',
            'El Melón',
            'El Quisco',
            'El Tabo',
            'Hanga Roa',
            'Hijuelas',
            'La Calera',
            'La Cruz',
            'La Ligua',
            'Las Ventanas',
            'Limache',
            'Llaillay',
            'Los Andes',
            'Nogales',
            'Olmué',
            'Putaendo',
            'Quillota',
            'Quilpué',
            'Quintero',
            'Rinconada',
            'San Antonio',
            'San Esteban',
            'Santa María',
            'Santo Domingo',
            'Valparaíso',
            'Villa Alemana',
            'Villa Los Almendros',
            'Viña Del Mar',
        ]
    },
    {
        region: 'Metropolitana',
        places: [
            'todo',
            'Alto Jahuel',
            'Bajos De San Agustín',
            'Batuco',
            'Buin',
            'Cerrillos',
            'Cerro Navía',
            'Colina',
            'Conchalí',
            'Curacaví',
            'El Bosque',
            'El Monte',
            'Estación Central',
            'Hospital',
            'Huechuraba',
            'Independencia',
            'Isla De Maipo',
            'La Cisterna',
            'La Florida',
            'La Granja',
            'La Islita',
            'La Pintana',
            'La Reina',
            'Lampa',
            'Las Condes',
            'Lo Barnechea',
            'Lo Espejo',
            'Lo Prado',
            'Macul',
            'Maipú',
            'Melipilla',
            'Ñuñoa',
            'Padre Hurtado',
            'Paine',
            'Pedro Aguirre Cerda',
            'Peñaflor',
            'Peñalolén',
            'Pirque',
            'Providencia',
            'Pudahuel',
            'Puente Alto',
            'Quilicura',
            'Quinta Normal',
            'Recoleta',
            'Renca',
            'San Bernardo',
            'San Joaquín',
            'San José De Maipo',
            'San Miguel',
            'San Ramón',
            'Santiago',
            'Talagante',
            'Tiltil',
            'Vitacura'
        ]
    },
    {
        region: "O'Higgins",
        places: [
            'todo',
            'Codegua',
            'Doñihue',
            'Graneros',
            'Gultro',
            'Cabras',
            'Lo Miranda',
            'Machalí',
            'Nancagua',
            'Palmilla',
            'Peumo',
            'Pichilemu',
            'Punta Diamante',
        ]
    },
    {
        region: 'Maule',
        places: [
            'todo',
            'Cauquenes',
            'Constitución',
            'Curicó',
            'Hualañé',
            'Linares',
            'Longaví',
            'Molina',
            'Parral',
            'San Clemente',
            'San Javier',
            'Talca',
            'Teno',
            'Villa Alegre',
        ]
    },
    {
        region: 'Biobío',
        places: [
            'todo',
            'Arauco',
            'Bulnes',
            'Cabrero',
            'Cañete',
            'Chiguayante',
            'Chillán',
            'Coelemu',
            'Coihueco',
            'Concepción',
            'Coronel',
            'Curanilahue',
            'Hualpén',
            'Hualqui',
            'Lebu',
            'Los Ángeles',
        ],
    },
    {
        region: 'Araucanía',
        places: [
            'todo',
            'Angol',
            'Carahue',
            'Collipulli',
            'Cunco',
            'Curacautín',
            'Freire',
            'Gorbea',
            'Labranza',
            'Lautaro',
            'Loncoche',
            'Nueva Imperial',
            'Padre Las Casas',
            'Pitrufquén',
            'Pucón',
            'Purén',
            'Renaico',
            'Temuco',
            'Traiguén',
            'Victoria',
            'Villarrica'
        ]
    },
    {
        region: 'Los Ríos',
        places: [
            'todo',
            'Futrono',
            'La Unión',
            'Lanco',
            'Los Lagos',
            'Paillaco',
            'Panguipulli',
            'Río Bueno',
            'San José De La Mariquina',
            'Valdivia',
        ]
    },
    {
        region: 'Los Lagos',
        places: [
            'todo',
            'Ancud',
            ' Calbuco',
            'Castro',
            'Fresia',
            'Frutillar',
            'Llanquihue',
            'Los Muermos',
            'Osorno',
            'Puerto Montt',
            'Puerto Varas',
            'Purranque',
            'Quellón',
            'Río Negro'
        ]
    },
    {
        region: 'Magallanes',
        places: [
            'todo',
            'Puerto Natales',
            'Punta Arenas'
        ]
    }
]

// este es el togle
const toggle_show = document.getElementById('toggle-show')

// Esta es la seleccion completa del select
const select_item1 = document.getElementById('select-item1')
const select_item2 = document.getElementById('select-item2')
const select_item3 = document.getElementById('select-item3')

// Entradas de texto del select
const input_select1 = document.getElementById('input_select1')
const input_select2 = document.getElementById('input_select2')
const input_select3 = document.getElementById('input_select3')




// activa i muestra el menu select
select_item1.addEventListener('click',function() {
    select_item1.classList.contains('activate') ? select_item1.classList.remove('activate') : select_item1.classList.add('activate')
})
select_item2.addEventListener('click',function() {
    select_item2.classList.contains('activate') ? select_item2.classList.remove('activate') : select_item2.classList.add('activate')
})
select_item3.addEventListener('click',function() {
    select_item3.classList.contains('activate') ? select_item3.classList.remove('activate') : select_item3.classList.add('activate')
})



const pro = ['todo']
const cl3 = document.getElementById('content-links')
// generacion por defecto del ultimo selector
function show(array,region_r) {
    let element = ''
    array.forEach((e) => {
        element += ` 
        <div class="content-link content-link-pro">
            <i class="fa-solid fa-arrow-right"></i>
            <li>${e}</li>
        </div>
        `
    });
    region_r.innerHTML = element
}

show(pro,cl3);



const content_link = document.getElementsByClassName('content-link-status')
for(op of content_link) {
    op.onclick = function() {
        input_select1.innerHTML = this.textContent
    }
}
const content_link_con = document.getElementsByClassName('content-link-con')
for(op of content_link_con) {
    op.onclick = function() {
        input_select2.innerHTML = this.textContent
        // cambio en el input 3
        //show(protest,cl3);
        //console.log(this.innerText)
        chile_places.filter((e) => {
            //console.log(e.region.trim())
            //console.log(this.innerHTML.trim())
            if(e.region === this.innerText) {
                show(e.places,cl3)
                if(e.places.length > 5 && !toggle_show.classList.contains('toggle-scroll')) {
                    toggle_show.classList.add('toggle-scroll')
                }else {
                    toggle_show.classList.remove('toggle-scroll')
                }
            }
        })
        let content_link_pro = document.getElementsByClassName('content-link-pro')
        for(op of content_link_pro) {
            op.onclick = function() {
                input_select3.innerHTML = this.textContent
            }
        }
    }
}


// BUscar la seleccion del botton
$(document).ready(function () {
    
    $("#formSelect").submit(function (event) {
        event.preventDefault();

        let form  = {
            region: 'Concepcion',
            city: 'todo',
            status: "Arriendo"
        }
        console.log(form)
        
        $.ajax({
            url: window.location.pathname,
            type: "POST",
            data: form,    
            processData: false,
            contentType: false,
            success: function (data) {
                //console.log(data);
            }
        }); 
    })
})







