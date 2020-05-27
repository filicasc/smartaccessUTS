<div class="alert alert-success" role="alert">
    <strong>{{$slot}}</strong>
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
    </button>
</div>

<script>
    $('document').ready( () => {
        $('div.alert').fadeOut(5000);
    });
</script>
