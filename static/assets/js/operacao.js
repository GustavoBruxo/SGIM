function ConvertDatas(rawDate) {
    var dateArray = rawDate.split("/");
    var parsedDate = dateArray[2] + dateArray[1] + dateArray[0];
    return parsedDate;
}

$(document).ready(function () {
    moment.locale('pt-br');
    $(function() {
        var start = moment().subtract(29, 'days');
        var end = moment();
    
        function cb(start, end) {
            $('#reportrange span').html(start.format('DD/MM/YYYY') + ' - ' + end.format('DD/MM/YYYY'));
        }
    
        $('#reportrange').daterangepicker({
            startDate: start,
            endDate: end,
            locale: {
                "format": 'DD/MM/YYYY',
                "applyLabel": 'Confirmar',
                "cancelLabel": 'Cancelar',
                "fromLabel": "De",
                "toLabel": "Até",
                "customRangeLabel": "Datas",
                "daysOfWeek": ["Dom","Seg","Ter", "Qua", "Qui","Sex","Sab"],
                "monthNames": [ "Jan","Fev","Mar","Abr","Mai","Jun", "Jul","Ago","Set","Out", "Nov","Dez"],
                "firstDay" : 0
              },
            ranges: {
                'Hoje': [moment(), moment()],
                'Ontem': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                'Ùltimos 7 dias': [moment().subtract(6, 'days'), moment()],
                'Ùltimos 30 dias': [moment().subtract(29, 'days'), moment()],
                'Mês Atual': [moment().startOf('month'), moment().endOf('month')],
                'Mês Anterior': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
            }
        }, cb);
    
        cb(start, end);
    
    });

    $('#reportrange').on('apply.daterangepicker', function(ev, picker) {
        var start = moment(picker.startDate).format('DD/MM/YYYY');
        var end = moment(picker.endDate).format('DD/MM/YYYY');

        $.fn.dataTable.ext.search.push(
            function (settings, data, dataIndex) {
                var dateStart = ConvertDatas(start);
                var dateEnd = ConvertDatas(end);
                var evalDate = ConvertDatas(data[3].trim());

                if ((isNaN(dateStart)) || (isNaN(dateEnd))) {
                    return true;
                }
                if (evalDate >= dateStart && evalDate <= dateEnd) {
                    return true;
                } else {
                    return false;
                }
            }
        );
        table.draw();
        $.fn.dataTable.ext.search.pop();
    });

    var table = $('#operacoes').DataTable({
        responsive: true, // Datatable Responsivo
        dom: '<"top"l>frtip<"bottom"B>', // Posição dos itens da Datatable
        buttons: [ // Botões
            {
                extend: 'excelHtml5',
                className: 'btn btn-success',
            },
            {
                extend: 'pdfHtml5',
                className: 'btn btn-danger',
            },],
        aaSorting: [], // Não vai organizar de forma automatica, mas sim pelo backend
        pageLength: 30, // Nº de itens por página
        columnDefs: [{
            targets: [5, 6],
            orderable: false
        }], // Colunas sem a opção de ordenação
        language: {
            emptyTable: "Nenhum registro encontrado",
            info: "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            infoFiltered: "(Filtrados de _MAX_ registros)",
            infoThousands: ".",
            loadingRecords: "Carregando...",
            zeroRecords: "Nenhum registro encontrado",
            search: "Pesquisar",
            processing: "Carregando...",
            searchPlaceholder: "Buscar registros",
            paginate: {
                next: "Próximo",
                previous: "Anterior",
                first: "Primeiro",
                last: "Último"
            },
            lengthMenu: "Exibir _MENU_ resultados por página",
            infoEmpty: "Mostrando 0 até 0 de 0 registro(s)"
        },
    });

    $('#search').keyup(function () {
        table.search($(this).val()).draw();
    });

    $('#min, #max').change(function() {
        table.draw();
    });

    setTimeout(function () {
        table.columns.adjust().draw();
    }, 2000);
});