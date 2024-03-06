import graphene
from graphene_django import DjangoObjectType
from app.models import Empresa, Cargo, Funcionario, Produto

class EmpresaType(DjangoObjectType):
    class Meta:
        model = Empresa
        fields = "__all__"

class CargoType(DjangoObjectType):
    class Meta:
        model = Cargo
        fields = "__all__"

class FuncionarioType(DjangoObjectType):
    class Meta:
        model = Funcionario
        fields = "__all__"

class ProdutoType(DjangoObjectType):
    class Meta:
        model = Produto
        fields = "__all__"

class EmpresaInput(graphene.InputObjectType):
    nome = graphene.String(required=True)

class CargoInput(graphene.InputObjectType):
    nome = graphene.String(required=True)

class FuncionarioInput(graphene.InputObjectType):
    nome = graphene.String(required=True)
    empresa_id = graphene.ID(required=True)
    cargo_id = graphene.ID(required=True)

class ProdutoInput(graphene.InputObjectType):
    nome = graphene.String(required=True)
    preco = graphene.Decimal(required=True)
    descricao = graphene.String(required=True)

class CreateEmpresa(graphene.Mutation):
    class Arguments:
        input = EmpresaInput(required=True)

    empresa = graphene.Field(EmpresaType)

    def mutate(root, info, input):
        empresa = Empresa.objects.create(nome=input.nome)
        return CreateEmpresa(empresa=empresa)

class CreateCargo(graphene.Mutation):
    class Arguments:
        input = CargoInput(required=True)

    cargo = graphene.Field(CargoType)

    def mutate(root, info, input):
        cargo = Cargo.objects.create(nome=input.nome)
        return CreateCargo(cargo=cargo)

class CreateFuncionario(graphene.Mutation):
    class Arguments:
        input = FuncionarioInput(required=True)

    funcionario = graphene.Field(FuncionarioType)

    def mutate(root, info, input):
        empresa = Empresa.objects.get(id=input.empresa_id)
        cargo = Cargo.objects.get(id=input.cargo_id)
        funcionario = Funcionario.objects.create(nome=input.nome, empresa=empresa, cargo=cargo)
        return CreateFuncionario(funcionario=funcionario)

class CreateProduto(graphene.Mutation):
    class Arguments:
        input = ProdutoInput(required=True)

    produto = graphene.Field(ProdutoType)

    def mutate(root, info, input):
        produto = Produto.objects.create(nome=input.nome, preco=input.preco, descricao=input.descricao)
        return CreateProduto(produto=produto)
class UpdateEmpresa(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = EmpresaInput(required=True)

    empresa = graphene.Field(EmpresaType)

    def mutate(root, info, id, input):
        empresa = Empresa.objects.get(id=id)
        empresa.nome = input.nome
        empresa.save()
        return UpdateEmpresa(empresa=empresa)

class UpdateCargo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = CargoInput(required=True)

    cargo = graphene.Field(CargoType)

    def mutate(root, info, id, input):
        cargo = Cargo.objects.get(id=id)
        cargo.nome = input.nome
        cargo.save()
        return UpdateCargo(cargo=cargo)

class UpdateFuncionario(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = FuncionarioInput(required=True)

    funcionario = graphene.Field(FuncionarioType)

    def mutate(root, info, id, input):
        funcionario = Funcionario.objects.get(id=id)
        funcionario.nome = input.nome
        funcionario.empresa_id = input.empresa_id
        funcionario.cargo_id = input.cargo_id
        funcionario.save()
        return UpdateFuncionario(funcionario=funcionario)

class UpdateProduto(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ProdutoInput(required=True)

    produto = graphene.Field(ProdutoType)

    def mutate(root, info, id, input):
        produto = Produto.objects.get(id=id)
        produto.nome = input.nome
        produto.preco = input.preco
        produto.descricao = input.descricao
        produto.save()
        return UpdateProduto(produto=produto)

class DeleteEmpresa(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        empresa = Empresa.objects.get(id=id)
        empresa.delete()
        return DeleteEmpresa(success=True)

class DeleteCargo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        cargo = Cargo.objects.get(id=id)
        cargo.delete()
        return DeleteCargo(success=True)

class DeleteFuncionario(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        funcionario = Funcionario.objects.get(id=id)
        funcionario.delete()
        return DeleteFuncionario(success=True)

class DeleteProduto(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        produto = Produto.objects.get(id=id)
        produto.delete()
        return DeleteProduto(success=True)

class Query(graphene.ObjectType):
    empresas = graphene.List(EmpresaType)
    cargos = graphene.List(CargoType)
    funcionarios = graphene.List(FuncionarioType)
    produtos = graphene.List(ProdutoType)

    def resolve_empresas(root, info):
        return Empresa.objects.all()

    def resolve_cargos(root, info):
        return Cargo.objects.all()

    def resolve_funcionarios(root, info):
        return Funcionario.objects.all()

    def resolve_produtos(root, info):
        return Produto.objects.all()

class Mutation(graphene.ObjectType):
    create_empresa = CreateEmpresa.Field()
    create_cargo = CreateCargo.Field()
    create_funcionario = CreateFuncionario.Field()
    create_produto = CreateProduto.Field()
    update_empresa = UpdateEmpresa.Field()
    update_cargo = UpdateCargo.Field()
    update_funcionario = UpdateFuncionario.Field()
    update_produto = UpdateProduto.Field()
    delete_empresa = DeleteEmpresa.Field()
    delete_cargo = DeleteCargo.Field()
    delete_funcionario = DeleteFuncionario.Field()
    delete_produto = DeleteProduto.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
