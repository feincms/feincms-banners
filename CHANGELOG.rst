Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

- Added ``HTTP_X_FORWARDED_FOR`` checking before ``REMOTE_ADDR`` for
  determining the remote IP of clicks.
- Removed code for really old Django versions. Dropped South migrations
  from the tree, regenerated migrations using a newer Django version for
  better compatbility.
- Reformatted the code using black.


`1.2`_ (2014-09-25)
~~~~~~~~~~~~~~~~~~~

- The version where this changelog starts.


.. _1.2: https://github.com/feincms/feincms-banners/commit/3d094f98187
.. _Next version: https://github.com/feincms/feincms-banners/compare/0.1...master
