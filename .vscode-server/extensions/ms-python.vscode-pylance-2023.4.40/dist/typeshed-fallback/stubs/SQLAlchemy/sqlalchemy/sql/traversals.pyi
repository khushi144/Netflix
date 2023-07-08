from typing import Any

from .. import util
from ..util import HasMemoized
from .visitors import ExtendedInternalTraversal, InternalTraversal

SKIP_TRAVERSE: Any
COMPARE_FAILED: bool
COMPARE_SUCCEEDED: bool
NO_CACHE: Any
CACHE_IN_PLACE: Any
CALL_GEN_CACHE_KEY: Any
STATIC_CACHE_KEY: Any
PROPAGATE_ATTRS: Any
ANON_NAME: Any

def compare(obj1, obj2, **kw): ...

class HasCacheKey:
    inherit_cache: Any

class MemoizedHasCacheKey(HasCacheKey, HasMemoized): ...

class CacheKey:
    def __hash__(self) -> int: ...
    def to_offline_string(self, statement_cache, statement, parameters): ...
    def __eq__(self, other): ...

class _CacheKey(ExtendedInternalTraversal):
    visit_has_cache_key: Any
    visit_clauseelement: Any
    visit_clauseelement_list: Any
    visit_annotations_key: Any
    visit_clauseelement_tuple: Any
    visit_memoized_select_entities: Any
    visit_string: Any
    visit_boolean: Any
    visit_operator: Any
    visit_plain_obj: Any
    visit_statement_hint_list: Any
    visit_type: Any
    visit_anon_name: Any
    visit_propagate_attrs: Any
    def visit_with_context_options(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_inspectable(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_string_list(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_multi(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_multi_list(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_has_cache_key_tuples(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_has_cache_key_list(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_executable_options(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_inspectable_list(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_clauseelement_tuples(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_fromclause_ordered_set(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_clauseelement_unordered_set(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_named_ddl_element(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_prefix_sequence(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_setup_join_tuple(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_table_hint_list(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_plain_dict(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_dialect_options(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_string_clauseelement_dict(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_string_multi_dict(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_fromclause_canonical_column_collection(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_unknown_structure(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_dml_ordered_values(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_dml_values(self, attrname, obj, parent, anon_map, bindparams): ...
    def visit_dml_multi_values(self, attrname, obj, parent, anon_map, bindparams): ...

class HasCopyInternals: ...

class _CopyInternals(InternalTraversal):
    def visit_clauseelement(self, attrname, parent, element, clone=..., **kw): ...
    def visit_clauseelement_list(self, attrname, parent, element, clone=..., **kw): ...
    def visit_clauseelement_tuple(self, attrname, parent, element, clone=..., **kw): ...
    def visit_executable_options(self, attrname, parent, element, clone=..., **kw): ...
    def visit_clauseelement_unordered_set(self, attrname, parent, element, clone=..., **kw): ...
    def visit_clauseelement_tuples(self, attrname, parent, element, clone=..., **kw): ...
    def visit_string_clauseelement_dict(self, attrname, parent, element, clone=..., **kw): ...
    def visit_setup_join_tuple(self, attrname, parent, element, clone=..., **kw): ...
    def visit_memoized_select_entities(self, attrname, parent, element, **kw): ...
    def visit_dml_ordered_values(self, attrname, parent, element, clone=..., **kw): ...
    def visit_dml_values(self, attrname, parent, element, clone=..., **kw): ...
    def visit_dml_multi_values(self, attrname, parent, element, clone=..., **kw): ...
    def visit_propagate_attrs(self, attrname, parent, element, clone=..., **kw): ...

class _GetChildren(InternalTraversal):
    def visit_has_cache_key(self, element, **kw): ...
    def visit_clauseelement(self, element, **kw): ...
    def visit_clauseelement_list(self, element, **kw): ...
    def visit_clauseelement_tuple(self, element, **kw): ...
    def visit_clauseelement_tuples(self, element, **kw): ...
    def visit_fromclause_canonical_column_collection(self, element, **kw): ...
    def visit_string_clauseelement_dict(self, element, **kw): ...
    def visit_fromclause_ordered_set(self, element, **kw): ...
    def visit_clauseelement_unordered_set(self, element, **kw): ...
    def visit_setup_join_tuple(self, element, **kw) -> None: ...
    def visit_memoized_select_entities(self, element, **kw): ...
    def visit_dml_ordered_values(self, element, **kw) -> None: ...
    def visit_dml_values(self, element, **kw) -> None: ...
    def visit_dml_multi_values(self, element, **kw): ...
    def visit_propagate_attrs(self, element, **kw): ...

class anon_map(dict[Any, Any]):
    index: int
    def __init__(self) -> None: ...
    def __missing__(self, key): ...

class TraversalComparatorStrategy(InternalTraversal, util.MemoizedSlots):
    stack: Any
    cache: Any
    anon_map: Any
    def __init__(self) -> None: ...
    def compare(self, obj1, obj2, **kw): ...
    def compare_inner(self, obj1, obj2, **kw): ...
    def visit_has_cache_key(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_propagate_attrs(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_has_cache_key_list(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_executable_options(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_clauseelement(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_fromclause_canonical_column_collection(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_fromclause_derived_column_collection(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_string_clauseelement_dict(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_clauseelement_tuples(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_clauseelement_list(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_clauseelement_tuple(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_clauseelement_unordered_set(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_fromclause_ordered_set(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_string(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_string_list(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_anon_name(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_boolean(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_operator(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_type(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_plain_dict(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_dialect_options(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_annotations_key(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_with_context_options(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_plain_obj(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_named_ddl_element(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_prefix_sequence(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_setup_join_tuple(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_memoized_select_entities(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_table_hint_list(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_statement_hint_list(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_unknown_structure(self, attrname, left_parent, left, right_parent, right, **kw) -> None: ...
    def visit_dml_ordered_values(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_dml_values(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def visit_dml_multi_values(self, attrname, left_parent, left, right_parent, right, **kw): ...
    def compare_clauselist(self, left, right, **kw): ...
    def compare_binary(self, left, right, **kw): ...
    def compare_bindparam(self, left, right, **kw): ...

class ColIdentityComparatorStrategy(TraversalComparatorStrategy):
    def compare_column_element(self, left, right, use_proxies: bool = True, equivalents=(), **kw): ...
    def compare_column(self, left, right, **kw): ...
    def compare_label(self, left, right, **kw): ...
    def compare_table(self, left, right, **kw): ...
