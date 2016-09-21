$(document).ready ( function () {
	st = new Sitio()
})

function Sitio() {

	this.calendario = $('#calendario');

	this.modal = $('#win_calendar');

	this.Init();
}
Sitio.prototype.Init = function () {
	

	this.calendario.fullCalendar({
    	weekends: false,
    	locale: 'es',
    	dayClick: this.Click_Dia,
	});	

	this.modal.on('shown.bs.modal',this, this.Dibuja_Calendario)	
}
Sitio.prototype.Dibuja_Calendario = function(e) {


 	// : function() {
  //       alert('a day has been clicked!');
  //   }

    e.data.calendario.fullCalendar('today');
}
Sitio.prototype.Click_Dia = function(date, event, view) {

	anio = date.format("YYYY");
	mes = date.format("M");
	dia = date.format("D");

	var url = '/reservacion/nueva/'+anio+'/'+mes+'/'+dia+'/'

	// alert(url);

	window.location.href = url
}