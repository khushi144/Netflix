from _typeshed import Incomplete
from typing import Any, Generic, TypeVar

from .. import util
from ..sql import operators, roles
from ..sql.base import ExecutableOption
from ..sql.traversals import HasCacheKey
from .base import (
    EXT_CONTINUE as EXT_CONTINUE,
    EXT_SKIP as EXT_SKIP,
    EXT_STOP as EXT_STOP,
    MANYTOMANY as MANYTOMANY,
    MANYTOONE as MANYTOONE,
    NOT_EXTENSION as NOT_EXTENSION,
    ONETOMANY as ONETOMANY,
    InspectionAttr as InspectionAttr,
    InspectionAttrInfo as InspectionAttrInfo,
    _MappedAttribute as _MappedAttribute,
)

_T = TypeVar("_T")

__all__ = (
    "EXT_CONTINUE",
    "EXT_STOP",
    "EXT_SKIP",
    "ONETOMANY",
    "MANYTOMANY",
    "MANYTOONE",
    "NOT_EXTENSION",
    "LoaderStrategy",
    "MapperOption",
    "LoaderOption",
    "MapperProperty",
    "PropComparator",
    "StrategizedProperty",
)

class ORMStatementRole(roles.StatementRole): ...
class ORMColumnsClauseRole(roles.ColumnsClauseRole): ...
class ORMEntityColumnsClauseRole(ORMColumnsClauseRole): ...
class ORMFromClauseRole(roles.StrictFromClauseRole): ...

class MapperProperty(HasCacheKey, _MappedAttribute, InspectionAttr, util.MemoizedSlots):
    cascade: Any
    is_property: bool
    key: Incomplete
    info: Incomplete
    def setup(self, context, query_entity, path, adapter, **kwargs) -> None: ...
    def create_row_processor(self, context, query_entity, path, mapper, result, adapter, populators) -> None: ...
    def cascade_iterator(self, type_, state, dict_, visited_states, halt_on: Incomplete | None = None): ...
    parent: Any
    def set_parent(self, parent, init) -> None: ...
    def instrument_class(self, mapper) -> None: ...
    def __init__(self) -> None: ...
    def init(self) -> None: ...
    @property
    def class_attribute(self): ...
    def do_init(self) -> None: ...
    def post_instrument_class(self, mapper) -> None: ...
    def merge(
        self, session, source_state, source_dict, dest_state, dest_dict, load, _recursive, _resolve_conflict_map
    ) -> None: ...

class PropComparator(operators.ColumnOperators[_T], Generic[_T]):
    __visit_name__: str
    prop: Any
    property: Any
    def __init__(self, prop, parentmapper, adapt_to_entity: Incomplete | None = None) -> None: ...
    def __clause_element__(self) -> None: ...
    def adapt_to_entity(self, adapt_to_entity): ...
    @property
    def adapter(self): ...
    @property
    def info(self): ...
    @staticmethod
    def any_op(a, b, **kwargs): ...
    @staticmethod
    def has_op(a, b, **kwargs): ...
    @staticmethod
    def of_type_op(a, class_): ...
    def of_type(self, class_): ...
    def and_(self, *criteria): ...
    def any(self, criterion: Incomplete | None = None, **kwargs): ...
    def has(self, criterion: Incomplete | None = None, **kwargs): ...

class StrategizedProperty(MapperProperty):
    inherit_cache: bool
    strategy_wildcard_key: Any
    def setup(self, context, query_entity, path, adapter, **kwargs) -> None: ...
    def create_row_processor(self, context, query_entity, path, mapper, result, adapter, populators) -> None: ...
    strategy: Any
    def do_init(self) -> None: ...
    def post_instrument_class(self, mapper) -> None: ...
    @classmethod
    def strategy_for(cls, **kw): ...

class ORMOption(ExecutableOption):
    propagate_to_loaders: bool

class CompileStateOption(HasCacheKey, ORMOption):
    def process_compile_state(self, compile_state) -> None: ...
    def process_compile_state_replaced_entities(self, compile_state, mapper_entities) -> None: ...

class LoaderOption(CompileStateOption):
    def process_compile_state_replaced_entities(self, compile_state, mapper_entities) -> None: ...
    def process_compile_state(self, compile_state) -> None: ...

class CriteriaOption(CompileStateOption):
    def process_compile_state(self, compile_state) -> None: ...
    def get_global_criteria(self, attributes) -> None: ...

class UserDefinedOption(ORMOption):
    propagate_to_loaders: bool
    payload: Any
    def __init__(self, payload: Incomplete | None = None) -> None: ...

class MapperOption(ORMOption):
    propagate_to_loaders: bool
    def process_query(self, query) -> None: ...
    def process_query_conditionally(self, query) -> None: ...

class LoaderStrategy:
    parent_property: Any
    is_class_level: bool
    parent: Any
    key: Any
    strategy_key: Any
    strategy_opts: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, **kwargs) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...
