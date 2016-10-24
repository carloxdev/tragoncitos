var url_dominio = window.location.protocol + '//' + window.location.host + '/'
var mes = 0
var anio = 0

$(document).ready ( function () {
	st = new Sitio()
})

function Sitio() {

	this.calendario = $('#calendario');
	this.modal = $('#win_calendar');
	this.kFields = null;
	this.kFuenteDatos = null;

	this.Init();
}
Sitio.prototype.Init = function () {

	this.kFields = {
        dia: { editable: false, type:"string"},
        descripcion: { editable: false, type: "string" },
	}

    this.kFuenteDatos = new kendo.data.DataSource({

        serverFiltering: true,
        transport: {
            read: {
                async: false,
                url: url_dominio + "api/menus/",
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return {
                        anio: anio,
                        mes: mes,
                    };
                }
            }
        },
        schema: {
            model: {
                id: "dia",
                fields: this.kfields
            }
        },
        error: function (e) {
            alert("Status: " + e.status + "; Error message: " + e.errorThrown);
        }
    });

	this.calendario.fullCalendar({
    	weekends: false,
    	locale: 'es',
    	// eventClick: this.click_Evento,
    	viewRender: this.change_Month,
	});	

	this.modal.on('shown.bs.modal',this, this.dibuja_Calendario)
}
Sitio.prototype.dibuja_Calendario = function(e) {
    e.data.calendario.fullCalendar('today');

}
Sitio.prototype.click_Evento = function(calEvent, jsEvent, view) {

	anio = calEvent.start.format("YYYY")
	mes = calEvent.start.format("M")
	dia = calEvent.start.format("D")

	var url = '/comanda/reservaciones/nueva/'+anio+'/'+mes+'/'+dia+'/'
	window.location.href = url
}
Sitio.prototype.change_Month = function(view, element) {

	st.calendario.fullCalendar("removeEvents");

	anio = view.intervalEnd.year()

	if (mes == view.intervalEnd.month()) {
		mes = view.intervalEnd.month() +1;
	}
	else
	{
		mes = view.intervalEnd.month();
	}

	// Buscar Menus x Mes
	st.kFuenteDatos.data([]);
	st.kFuenteDatos.read();
	
	datos = st.kFuenteDatos.data();

	var fecha = new Date()
	var fecha_dia = fecha.getDate()
	var fecha_mes = fecha.getMonth() + 1
	var fecha_anio = fecha.getFullYear()
	var fecha_actual = moment(fecha_anio +"-"+ fecha_mes +"-"+ fecha_dia, "YYYY-MM-DD")

	datos.forEach(function (elemento) {
		var nuevoEvento = new Object()
		nuevoEvento.title = "Menu";
		nuevoEvento.start = elemento.dia + "T00:00:00";

		var fecha_elemento = moment(elemento.dia, "YYYY-MM-DD");

		// console.log("fecha_actual: " + fecha_actual.format("DD/MM/YYYY"))
		// console.log("fecha_elemento: " + fecha_elemento.format("DD/MM/YYYY"))
		// console.log(fecha_elemento.isSameOrAfter(fecha_actual))
		// console.log(fecha_elemento.isSameOrBefore(fecha_actual))

		if (fecha_elemento.isSameOrAfter(fecha_actual)) {
			nuevoEvento.color = "#33861A";
			fecha_elemento_anio = fecha_elemento.format('YYYY')
			fecha_elemento_mes = fecha_elemento.format('MM')
			fecha_elemento_dia = fecha_elemento.format('DD')
			nuevoEvento.url = '/comanda/reservaciones/nueva/'+fecha_elemento_anio+'/'+fecha_elemento_mes+'/'+fecha_elemento_dia+'/'
		}
		else {
			nuevoEvento.color = "#6D7B82";
		}

		nuevoEvento.allDay = true;

		st.calendario.fullCalendar('renderEvent', nuevoEvento, true)
	});
}