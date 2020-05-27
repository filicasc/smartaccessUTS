@extends('layouts.dashboard')

@section('content')
<!-- TABLE: LATEST ORDERS -->
<div class="card">
    <div class="card-header border-transparent">
        <h3 class="card-title">Your codes</h3>

        <div class="card-tools">
            <button type="button" class="btn btn-tool" data-card-widget="collapse">
                <i class="fa fa-minus"></i>
            </button>
        </div>
    </div>
    <!-- /.card-header -->
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table m-0">
                <thead>
                <tr>
                    <th>Name visitor</th>
                    <th>Surname visitor</th>
                    <th>Type of code</th>
                    <th>Expiration date</th>
                    <th>Status</th>
                    <th>Access code</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>

                @forelse($codes as $code)
                    <tr>
                        <td>{{$code->name_visitor}}</td>
                        <td>{{$code->surname_visitor}}</td>
                        <td>{{$code->type}}</td>
                        <td>{{$code->expiration}}</td>
                        <td><span class="badge @if($code->status=='active') badge-success @else badge-danger @endif">{{$code->status}}</span></td>
                        <td>{{$code->access_code}}</td>
                        <td>
                            <form method="POST" action="{{route('code.destroy', $code->id)}}" class="d-inline">
                                @method('DELETE')
                                @csrf
                                <button type="submit" style="background:none; border:none; ">
                                    <i class="fa fa-2x fa-times text-red" aria-hidden="true"></i>
                                </button>
                            </form>
                            @if($code->status == 'active')
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{route('code.edit', $code->id)}}"><i class="fa fa-2x fa-pencil-square-o" aria-hidden="true"></i></a></td>
                            @endif
                    </tr>
                @empty
                    <tr>
                        <td colspan="7"> You didn't generate codes</td>
                    </tr>
                @endforelse
                </tbody>
            </table>
        </div>
        <!-- /.table-responsive -->
    </div>
    <!-- /.card-body -->
    <div class="card-footer clearfix">
        <div class="row">
            <div class="col-sm-6">
                {{$codes->links()}}
            </div>
            <div class="col-sm-6">
                <a href="javascript:void(0)" class="btn btn-sm btn-secondary float-right">View All Your Code</a>
            </div>
        </div>
    </div>
    <!-- /.card-footer -->
</div>
<!-- /.card -->
@endsection
