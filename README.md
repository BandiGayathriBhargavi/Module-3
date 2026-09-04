classDiagram
    %% --- DOMAIN LAYER (Innermost Core) ---
    class Entity {
        <<Domain Layer>>
        +Guid Id
        +Validate() bool
    }
    class ValueObject {
        <<Domain Layer>>
        +Equals(other) bool
    }
    class IRepository~T~ {
        <<Domain Layer - Interface>>
        +GetById(Guid id) T
        +Save(T entity) void
    }

    %% --- APPLICATION LAYER ---
    class Interactor_UseCase {
        <<Application Layer>>
        -IRepository~Entity~ repository
        -IOutputBoundary outputBoundary
        +Execute(InputData data) void
    }
    class InputBoundary {
        <<Application Layer - Interface>>
        +Execute(InputData data) void
    }
    class IOutputBoundary {
        <<Application Layer - Interface>>
        +Present(OutputData data) void
    }
    class InputData {
        <<Application Layer - DTO>>
        +String Field
    }
    class OutputData {
        <<Application Layer - DTO>>
        +String ResultField
    }

    %% --- INTERFACE ADAPTERS (Presentation / Controllers / Gateways) ---
    class Controller {
        <<Interface Adapters>>
        -InputBoundary inputBoundary
        +HandleRequest(HttpRequest request)
    }
    class Presenter {
        <<Interface Adapters>>
        -ViewModel viewModel
        +Present(OutputData data) void
    }
    class DataGateway {
        <<Interface Adapters>>
        -DbContext dbContext
        +GetById(Guid id) Entity
        +Save(Entity entity) void
    }

    %% --- INFRASTRUCTURE LAYER (Outermost Concerns) ---
    class DbContext {
        <<Infrastructure Layer>>
        +DbSet Entities
        +SaveChanges()
    }
    class WebFrameworkAPI {
        <<Infrastructure Layer>>
        +Route(String path)
    }

    %% --- RELATIONSHIPS & DEPENDENCY INVERSION (Pointing Inward) ---
    %% Domain Layer independence
    Entity ..> ValueObject : uses
    IRepository ..> Entity : manages

    %% Application Layer depends on Domain Layer
    Interactor_UseCase ..> Entity : manipulates
    Interactor_UseCase --> IRepository : uses (Dependency Inversion)
    Interactor_UseCase ..|> InputBoundary : implements
    Interactor_UseCase --> IOutputBoundary : uses

    %% Interface Adapters depend on Application Layer
    Controller --> InputBoundary : triggers
    Controller ..> InputData : constructs
    Presenter ..|> IOutputBoundary : implements
    Presenter ..> OutputData : consumes
    DataGateway ..|> IRepository : implements

    %% Infrastructure Layer depends on Interface Adapters / External Libraries
    DataGateway --> DbContext : wraps
    WebFrameworkAPI --> Controller : dispatches to
