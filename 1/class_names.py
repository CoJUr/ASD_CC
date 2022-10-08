# nouns for class names - avoid verbs
class Performer: pass # Peform or Performed: verb. no good
class Performance: pass # Performing: a verb. no good


# adjective prefixes to convey time
class ActivePerformance: pass
class PastPerformer: pass

# messy: adjectives
# class Huge:   class Small:   class Fast:    class Slow:

# cleaner - adjectives as prefixes to nouns
class SmallPerformance: pass
class FastPerformer: pass

# messy: vague prefixes
# class MyPerformance: class APerformance:  class ThePerformance:

# messy: single letter classnames/prefixes. exception: languages with templates
# class P:   class CPerformer:   class TPerformer:

# messy: plurals on normal classes. use only for collection or container
# classes
class Performers:
    def __getitem__(self, key): pass
    def __iter__(self): pass

